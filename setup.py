from setuptools import setup, find_packages

setup(
    name = "houdini-lexers",
    version = "1.0",
    packages = find_packages(),
    description = 'This package contains the pygments lexer for the vex language used in Houdini',
    author = 'SideFX Software Inc.',
    author_email = 'pirave@sidefx.com',
    url = 'https://github.com/pirave/houdini-lexers'
    download_url = 'https://github.com/pirave/houdini-lexers/tarball/1.0',
    install_requires="Pygments",
    entry_points="""
        [pygments.lexers]
        vex=lexers.vex:VexLexer
        hscript=lexers.vex:HScriptLexer
    """
)

# run python lexer_package_setup.py sdist to get a dist/HoudiniLexers-1.0.tar.gz file
# pip install dist/HoudiniLexers-1.0.tar.gz