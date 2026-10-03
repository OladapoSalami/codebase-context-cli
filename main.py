import click
from rich.console import Console
from rich.panel import Panel
from scanner import generate_context
import os
import pyperclip

console = Console()

@click.command()
@click.argument('path', default='.', type=click.Path(exists = True))
@click.option('-o', '--output', default='llm_context.md', help='Output Markdown file name')
@click.option('-c', '--copy', is_flag=True, help='Automatically copy the result to your clipboard')
def cli(path, output, copy):
    """Packs a codebase into a single Markdown file for LLM context."""

    with console.status(f"[bold green]Scanning directory {os.path.abspath(path)}...", spinner="dots"):
        output_path, file_count = generate_context(path, output)

    success_msg = f"Successfully packed [bold cyan]{file_count}[/bold cyan] files into [bold yellow]{output_path}[/bold yellow]"

    #Handle the clipboard copy action
    if copy:
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                content = f.read()
            pyperclip.copy(content)
            success_msg += "\n[bold magenta]✨ Copied directly to the clipboard![/bold magenta]"
        except Exception as e:
            success_msg += f"\n[bold red] Failed to copy to clipboard: {str(e)}[/bold red]"

    console.print(Panel(success_msg, title="[bold green]^_- Done", expand=False))

if __name__ == '__main__':
    cli()