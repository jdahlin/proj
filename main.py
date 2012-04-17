import os
shpath = '/usr/lib/gnome-shell'
os.environ['LD_PRELOAD'] = shpath + '/libgnome-shell.so'
os.environ['GI_TYPELIB_PATH'] = shpath

from gi.repository import Pango
from gi.repository import Gdk
from gi.repository import Gtk
from gi.repository import GtkSource
from gi.repository import Clutter
from gi.repository import GtkClutter
from gi.repository import St

orig = Clutter.Actor.add_child
def add_child(parent, actor, **props):
    orig(parent, actor)
    for key, value in props.items():
        parent.child_set_property(actor, key, value)
Clutter.Actor.add_child = add_child


class SourceViewArea(GtkClutter.Actor):
    def __init__(self):
        GtkClutter.Actor.__init__(self)

        self._create_language()
        self._create_buffer()
        self._create_ui()
        self.source_view.set_buffer(self.text_buffer)

    def _create_language(self):
        manager = GtkSource.LanguageManager.get_default()
        self.language = manager.get_language('python')

    def _create_buffer(self):
        self.text_buffer = GtkSource.Buffer()
        self.text_buffer.set_language(self.language)
        tag_table = self.text_buffer.get_tag_table()
        self._default_tag = Gtk.TextTag(name='default')
        tag_table.add(self._default_tag)
        self._default_tag.props.font = Pango.FontDescription('Ubuntu Mono 12')

    def _create_ui(self):
        bin = self.get_widget()
        self.show()

        sw = Gtk.ScrolledWindow()
        bin.add(sw)
        sw.show()

        self.source_view = GtkSource.View()
        sw.add(self.source_view)
        self.source_view.show()

    def add_from_file(self, filename):
        # FIXME: async
        fd = open(filename)
        text = fd.read()
        self.text_buffer.set_text(text)
        start, end = self.text_buffer.get_bounds()
        self.text_buffer.apply_tag(self._default_tag, start, end)

    def grab_focus(self):
        self.source_view.grab_focus()


class App:
    def __init__(self):
        self.setup()

    def setup(self):
        w = Gtk.Window()
        w.connect('destroy', lambda unused: Gtk.main_quit())
        w.connect('key-press-event', self.on_key_press_event)
        w.connect('window-state-event', self.on_window_state_event)
        w.fullscreen()

        self.clutter = GtkClutter.Embed()
        w.add(self.clutter)
        self.window = w
        self.window.show()

        self.stage = self.clutter.get_stage()
        context = St.ThemeContext.get_for_stage(self.stage)
        theme = St.Theme(application_stylesheet="test.css")
        context.set_theme(theme)

    def setup_boxes(self):
        window = self.window.get_window()
        rect = window.get_frame_extents()
        background = St.BoxLayout(style_class="background",
                                  width=rect.width,
                                  height=rect.height - 28)
        self.stage.add_child(background)

        left_box = St.BoxLayout(style_class="left_box")
        background.add_child(left_box, y_fill=False, y_align=St.Align.START)

        right_box = St.BoxLayout(style_class="right_box")
        background.add_child(right_box, expand=True,
                             x_align=St.Align.END, x_fill=False,
                             y_align=St.Align.START, y_fill=False)
        right_box.hide()

        box = St.BoxLayout(style_class="source_box")
        left_box.add_child(box, expand=True)

        self.clutter.show()

        self.create_source_view(box)

    def create_source_view(self, main_box):
        gtk_actor = SourceViewArea()
        main_box.add_child(gtk_actor, expand=True, x_fill=True,
                          )
        gtk_actor.add_from_file('example.py')
        gtk_actor.grab_focus()

    def on_key_press_event(self, window, event):
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()
            return True
        return False

    def on_window_state_event(self, window, flags):
        state = window.get_window().get_state()
        if state & Gdk.WindowState.FULLSCREEN:
            self.setup_boxes()

def main():
    GtkClutter.init([])
    App()
    Gtk.main()

main()
