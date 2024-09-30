import click
from apis.groq_api import GroqAPI
from apis.utils import get_git_diff
import logging

@click.group()
def cli():
    pass

@cli.command()
@click.option('--use-groq', is_flag=True, help='Use GROQ for processing.')
@click.option('--model-name', type=str, default='llama-3.1-8b-instant', help='Name of the model to use.')
def commit(use_groq, model_name):
    diff = get_git_diff()
    if not diff:
        logging.info("No staged changes found.")
        click.echo("No staged changes found.")
        return

    click.echo(f"Changes: \n{diff}")

    if use_groq:
        groq_api = GroqAPI()
        message = groq_api.generate_commit_message(diff, model_name)
        if message:
            logging.info(f"Generated commit message: \n{message}")
            click.echo(f"Generated commit message: \n{message}")
        else:
            logging.error("Failed to generate commit message. Please check the logs for more details.")
            click.echo("Failed to generate commit message. Please check the logs for more details.")
    else:
        logging.info("Not used any LLM")
        click.echo("Not used any LLM")

if __name__ == "__main__":
    cli()