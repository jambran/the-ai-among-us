"""
Code to run the server
"""

import argparse

import uvicorn

parser = argparse.ArgumentParser(
    prog="ai_among_us_server",
    description="Start the server for playing The AI Among Us",
)
parser.add_argument("-p", "--port", default=8080, type=int)


def main():
    """
    Run the server
    :return:
    """
    arguments = parser.parse_args()
    uvicorn.run(
        "src.backend_service.api:app",
        host="0.0.0.0",
        port=arguments.port,
        reload=True,
    )


if __name__ == "__main__":
    main()
