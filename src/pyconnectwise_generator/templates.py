from pathlib import Path

from jinja2 import Template

template_dir = Path(__file__).parent / "templates"

endpoint_template = Template((template_dir / "endpoint_template.py.jinja2").read_text())
manage_client_template = Template((template_dir / "manage_client_template.py.jinja2").read_text())
automate_client_template = Template((template_dir / "automate_client_template.py.jinja2").read_text())
