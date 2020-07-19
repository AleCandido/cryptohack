import sys
import re

import rich.console
import rich.markdown
import rich.traceback

out = rich.console.Console()
Md = rich.markdown.Markdown
rich.traceback.install()

if __name__ == "__main__":
    out.print(Md("# *Alessandro*'s cryptohack runner"))

    # load ingredients
    module = re.sub(".py$", "", sys.argv[1].replace("/", "."))
    out.print(Md("## Exercise Selected"))
    exercise = dict(name=module)
    out.print(exercise)

    _loaded = __import__(module, fromlist=["get_flag", "input_data"])
    get_flag, input_data = _loaded.get_flag, _loaded.input_data

    # log input
    out.print(Md("## Check Input"))
    out.print(input_data)

    # retrieve flag
    out.print(Md("## Get Flag\n\nStart hacking..."))
    flag = get_flag(input_data)

    # export
    out.print(Md("## Report Flag"))
    # out.print(flag)
    out.print(f"  [bold #68ca68]{flag}[/]")
