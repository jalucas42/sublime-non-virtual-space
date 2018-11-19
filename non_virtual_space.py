import sublime                                                                                                                       
import sublime_plugin                                                                                                                       
                                                                                                                       
class NvsAppendSpaceCommand(sublime_plugin.TextCommand):                                                                                                                       
                                                                                                                       
    def run(self, edit):                                                                                                                       
                                                                                                                       
        regions = reversed(self.view.find_all(r" *\n", sublime.IGNORECASE));                                                                                                                       
        for region in regions:                                                                                                                       
            if region.size() < 120:                                                                                                                       
                self.view.insert(edit,region.begin(), " " * (120-region.size()))                                                                                                                       
                                                                                                                       
        #self.view.erase_regions("virtual_space");                                                                                                                       
        #self.view.add_regions("virtual_space", list(regions), "comment");                                                                                                                       
                                                                                                                       
class NvsRemoveSpaceCommand(sublime_plugin.TextCommand):                                                                                                                       
                                                                                                                       
    def run(self, edit):                                                                                                                       
                                                                                                                       
        regions = reversed(self.view.find_all(r" *\n", sublime.IGNORECASE));                                                                                                                       
        for region in regions:                                                                                                                       
            self.view.replace(edit,region, "\n");
                                                                                                                       
        #self.view.erase_regions("virtual_space");                                                                                                                       
        #self.view.add_regions("virtual_space", list(regions), "comment");                                                                                                                       
                                                                                                                       
                                                                                                                       
#class NvsListener(sublime_plugin.ViewEventListener):                                                                                                                       
#                                                                                                                       
#    def on_modified(view):                                                                                                                       
#        print("Called on_modified");                                                                                                                       
        