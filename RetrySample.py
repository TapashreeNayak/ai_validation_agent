import logging
import pybreaker

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    retry_if_exception_type,
)

logger = logging.getLogger(__name__)

# Open after repeated qualifying failures.
llm_breaker = pybreaker.CircuitBreaker(
    fail_max=5,
    reset_timeout=30,
)

# Retry temporary failures.
@retry(
    retry=retry_if_exception_type(
        (TimeoutError, ConnectionError)
    ),
    stop=stop_after_attempt(3),
    wait=wait_random_exponential(
        multiplier=1,
        max=8,
    ),
    reraise=True,
)
def call_llm_with_retry(prompt):
    return llm_client.generate(
        prompt,
        timeout=30,  # Illustrative client API
    )


@llm_breaker
def call_llm(prompt):
    return call_llm_with_retry(prompt)


def generate_explanation(prompt, rule_findings):
    try:
        response = call_llm(prompt)

        logger.info("LLM explanation generated successfully")

        return {
            "status": "success",
            "explanation": response,
            "rule_findings": rule_findings,
        }

    except Exception:
        logger.exception(
            "LLM explanation failed; using safe fallback"
        )

        return {
            "status": "ai_review_pending",
            "explanation": None,
            "rule_findings": rule_findings,
            "message": (
                "AI explanation unavailable. "
                "Manual review is required."
            ),
        }