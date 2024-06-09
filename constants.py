# constants for project class

# BACKEND = 'BACKEND'
# FRONTEND = 'FRONTEND'
# IOS = 'IOS'
# ANDROID = 'ANDROID'

TYPE_CHOICE = (
    ('BACKEND', 'Back-end'),
    ('FRONTEND', 'Front-end'),
    ('IOS', 'Ios'),
    ('ANDROID', 'Android')
)

# constants for issue class
# LOW = 'LOW'
# MEDIUM = 'MEDIUM'
# HIGH = 'HIGH'

PRIORITY_CHOICES = (
    ('LOW', 'Low'),
    ('MEDIUM', 'Medium'),
    ('HIGH', 'High')
)

# BG = 'BUG'
# FEATURE = 'FEATURE'
# TASK = 'TASK'

TAG_CHOICES = (
    ('BUG', 'Bug'),
    ('FEATURE', 'Feature'),
    ('TASK', 'Task')
)

# TO_DO = 'TO_DO'
# IN_PROGRESS = 'IN_PROGRESS'
# FINISHED = 'FINISHED'

STATUS_CHOICES = (
    ('TO_DO', 'To Do'),
    ('IN_PROGRESS', 'In Progress'),
    ('FINISHED', 'Finished')
)