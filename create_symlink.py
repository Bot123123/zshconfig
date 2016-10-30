import os

new_zshrc = '%s/.zshrc' % os.path.dirname(os.path.abspath(__file__))
old_zshrc = '%s/.zshrc' % os.environ['HOME']

os.rename(old_zshrc, '%s.b' % old_zshrc)
os.symlink(new_zshrc, old_zshrc)