from setuptools import setup, find_packages

setup(
    name = "houdini-lexers",
    version = "1.2",
    packages = find_packages(),
    description = 'This package contains the pygments lexer for the vex language used in Houdini',
    author = 'SideFX Software Inc.',
    author_email = 'pirave@sidefx.com',
    url = 'https://github.com/pirave/houdini-lexers',
    download_url = 'https://github.com/pirave/houdini-lexers/tarball/1.2',
    install_requires="Pygments",
    entry_points="""
        [pygments.lexers]
        vex=houdini_lexers.vex:VexLexer
        hscript=houdini_lexers.vex:HScriptLexer
    """
)
