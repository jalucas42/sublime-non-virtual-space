import sublime
import sublime_plugin

class NvsAppendSpaceCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        regions = reversed(self.view.find_all(r"( *)\n", sublime.IGNORECASE));

        for region in regions:
            if region.size() < 120:
                tmp = self.view.substr(sublime.Region(region.begin()-1,region.begin()));
                print("tmp='"+tmp+"'");
                # Don't append whitespace to lines that end in backslash, such as shell script multi-line commands.
                if tmp != "\\":
                    self.view.insert(edit,region.end()-1, " " * (120-region.size()))

        self.view.erase_regions("virtual_space");


class NvsRemoveSpaceCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        regions = reversed(self.view.find_all(r" *\n", sublime.IGNORECASE));
        for region in regions:
            self.view.replace(edit,region, "\n");

        self.view.erase_regions("virtual_space");


class NvsMarkEolCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        regions = reversed(self.view.find_all(r" *\n", sublime.IGNORECASE));

        self.view.erase_regions("virtual_space");
        self.view.add_regions("virtual_space", list(regions), "comment");


#class NvsListener(sublime_plugin.ViewEventListener):
#
#    def on_modified(view):
#        print("Called on_modified");
        