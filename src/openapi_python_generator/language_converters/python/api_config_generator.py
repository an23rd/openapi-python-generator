from openapi_schema_pydantic import OpenAPI

from src.openapi_python_generator.language_converters.python.jinja_config import JINJA_ENV, API_CONFIG_TEMPLATE
from src.openapi_python_generator.models import APIConfig


def generate_api_config(data: OpenAPI) -> APIConfig:
    """
    Generate the API model.
    """
    return APIConfig(
        file_name="api_config",
        content=JINJA_ENV.get_template(API_CONFIG_TEMPLATE).render(**data.dict()),
    )