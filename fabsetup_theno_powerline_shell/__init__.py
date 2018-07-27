from fabsetup.fabutils import print_msg, run, subtask, suggest_localhost, task

from fabsetup_theno_powerline_shell.fabutils import checkup_git_repo
from fabsetup_theno_powerline_shell.fabutils import checkup_git_repos
from fabsetup_theno_powerline_shell.fabutils import install_file
from fabsetup_theno_powerline_shell.fabutils import install_user_command
from fabsetup_theno_powerline_shell._version import __version__


@subtask
def install_pip_package():
    run('pip install --user termdown')


@subtask
def install_command():
    install_user_command('termdown',
                         TIMER_FINISHED_MESSAGE='TIMER FINISHED')


@subtask
def show_termdown_usage():
    print('termdown is now installed\n')
    print_msg('    python -m termdown --help\n')
    print('for example: time a pomodoro session\n')
    print_msg('    termdown 25m')


@task
@suggest_localhost
def powerline_shell():
    '''Install or update powerline-shell.

    powerline-shell (https://github.com/b-ryan/powerline-shell) is a beautiful and useful prompt for your shell.

    Touched files, dirs, and installed packages:

        ~/.config/powerline-shell/config.json
    '''
    install_pip_package()
    install_command()
    show_termdown_usage()
