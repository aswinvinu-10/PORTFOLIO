from data import PROJECTS
from ui import heading, project_card

heading("Projects", "What each project does, how it works and what I built")

for i, project in enumerate(PROJECTS):
    project_card(project, accent=(i == 0))
