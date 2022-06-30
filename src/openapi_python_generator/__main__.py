from typing import Optional

import click

from openapi_python_generator import __version__
from openapi_python_generator.common import HTTPLibrary, AutoFormat
from openapi_python_generator.generate_data import generate_data


@click.command()
@click.argument("source")
@click.argument("output")
@click.option(
    "--library",
    default=HTTPLibrary.httpx,
    type=HTTPLibrary,
    help="HTTP library to use in the generation of the client.",
)
@click.option(
    "--autoformat",
    default=AutoFormat.black,
    type=AutoFormat,
    help="Option to choose which auto formatter is applied.",
)
@click.version_option(version=__version__)
def main(
    source: str,
    output: str,
    library: Optional[HTTPLibrary] = HTTPLibrary.httpx,
    autoformat: Optional[AutoFormat] = AutoFormat.black,
) -> None:
    """
    Generate Python code from an OpenAPI 3.0 specification.

    Provide a SOURCE (file or URL) containing the OpenAPI 3 specification and
    an OUTPUT path, where the resulting client is created.
    """
    generate_data(source, output, library, autoformat)


if __name__ == "__main__":  # pragma: no cover
    main()
