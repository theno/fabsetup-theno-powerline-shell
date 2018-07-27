from fabsetup.fabutils import env, print_msg, run, subtask, suggest_localhost
from fabsetup.fabutils import task
from fabsetup.utils import update_or_append_line
from fabsetup.utils import uncomment_or_update_or_append_line
from utils import flo

from fabsetup_theno_powerline_shell.fabutils import package
from fabsetup_theno_powerline_shell.fabutils import checkup_git_repo
from fabsetup_theno_powerline_shell.fabutils import checkup_git_repos
from fabsetup_theno_powerline_shell.fabutils import install_file
from fabsetup_theno_powerline_shell.fabutils import install_user_command
from fabsetup_theno_powerline_shell._version import __version__


@subtask
def setup_fonts_for_powerline_shell():
    repo_dir = checkup_git_repo('https://github.com/powerline/fonts.git',
                                name='powerline-fonts')
    run(flo('cd {repo_dir} && ./install.sh'))
#    run('fc-cache -vf ~/.local/share/fonts')
    prefix = 'URxvt*font: '
    from config import fontlist
    line = prefix + fontlist
    update_or_append_line(filename='~/.Xresources', prefix=prefix,
            new_line=line)
    if env.host_string == 'localhost':
        run('xrdb  ~/.Xresources')


@subtask
def install_pip_package():
    run('pip install --user powerline-shell')


@subtask
def install_config():
    install_file('~/.config/powerline-shell/config.json')


@subtask
def install_bash_enabler():
    bash_snippet = '~/.bashrc_powerline_shell'
    install_file(path=bash_snippet)
    prefix = flo('if [ -f {bash_snippet} ]; ')
    enabler = flo('if [ -f {bash_snippet} ]; then source {bash_snippet}; fi')
    uncomment_or_update_or_append_line(filename='~/.bashrc', prefix=prefix,
                                       new_line=enabler)


@task
@suggest_localhost
def powerline_shell():
    '''Install or update and set up powerline-shell prompt.

    powerline-shell (https://github.com/b-ryan/powerline-shell) is a beautiful
    and useful prompt for your shell.

    More infos:
     * https://github.com/b-ryan/powerline-shell
     * https://askubuntu.com/questions/283908/how-can-i-install-and-use-powerline-plugin

    Touched files, dirs, and installed packages:

        ~/.config/powerline-shell/config.json
        pip install powerline-shell
    '''
    assert env.host == 'localhost', 'This task cannot run on a remote host'
    setup_fonts_for_powerline_shell()
    install_pip_package()
    install_config()
    install_bash_enabler()
#
#     question = 'Use normal question mark (u003F) for untracked files instead '\
#         'of fancy "black question mark ornament" (u2753, which may not work)?'
#     if query_yes_no(question, default='yes'):
#         filename = '~/repos/powerline-shell/powerline-shell.py'
#         update_or_append_line(filename, keep_backup=False,
#                               prefix="        'untracked': u'\u2753',",
#                               new_line="        'untracked': u'\u003F',")
#         run(flo('chmod u+x  {filename}'))
