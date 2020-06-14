try:
    import fastapi
    from pydantic import BaseModel
except ModuleNotFoundError:
    print('Run "pip install -e .[server]" to install all dependencies for sts-server.')
from semtextsim.implementation import inject
from semtextsim.interface import Encoder, Comparer

app = fastapi.FastAPI(title="Semantic Text Similarity Server",
                      description="Server which allows comparing the semantic "
                                  "text similarity for text bodies.")
"""WSGI compliant application."""


class _ComparisonRequest(BaseModel):
    """Data model for comparison request"""
    text_1: str
    text_2: str


class _ComparisonResponse(BaseModel):
    """Data model for the response of the comparison request"""
    similarity: float


@app.post("/compare",
          response_model=_ComparisonResponse)
def _compare(comparison: _ComparisonRequest,
             encoder: Encoder = fastapi.Depends(lambda: inject(Encoder)),
             comparer: Comparer = fastapi.Depends(lambda: inject(Comparer))):
    """Calculate the semantic similarity for two given text bodies."""
    features = encoder.encode(comparison.text_1, comparison.text_2)
    return {"similarity": comparer.compare(*features)}


def main():
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, log_level="info")


if __name__ == "__main__":
    main()
