import os
import sys
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

import analyze

orig = Clutter.Actor.add_child
def add_child(parent, actor, **props):
    orig(parent, actor)
    for key, value in props.items():
        parent.child_set_property(actor, key, value)
Clutter.Actor.add_child = add_child


class TextArea(St.BoxLayout):
    def __init__(self):
        St.BoxLayout.__init__(self, style_class="source_box")

        self.gtk_actor = GtkClutter.Actor()
        self.add_child(self.gtk_actor, expand=True)

        GtkClutter.Actor.__init__(self)

        self.text_buffer = self.create_buffer()
        self._create_default_tags()
        self._create_ui()
        self.view.set_buffer(self.text_buffer)

    def _create_default_tags(self):
        tag_table = self.text_buffer.get_tag_table()
        self._default_tag = Gtk.TextTag(name='default')
        tag_table.add(self._default_tag)
        self._default_tag.props.font = Pango.FontDescription('Ubuntu Mono 12')

    def _create_ui(self):
        bin = self.gtk_actor.get_widget()
        self.gtk_actor.show()

        sw = Gtk.ScrolledWindow()
        bin.add(sw)
        sw.show()

        self.view = self.create_view()
        sw.add(self.view)
        self.view.show()

    # Public

    def add_from_file(self, filename):
        # FIXME: async
        fd = open(filename)
        text = fd.read()
        self.text_buffer.set_text(text)
        start, end = self.text_buffer.get_bounds()
        self.text_buffer.apply_tag(self._default_tag, start, end)

    def create_buffer(self):
        text_buffer = Gtk.TextBuffer()
        return text_buffer

    def create_view(self):
        view = Gtk.TextView()
        return view

    def set_content(self, content):
        self.text_buffer.props.text = content

    def get_content(self):
        return self.text_buffer.props.text

    def grab_focus(self):
        self.view.grab_focus()


class SourceViewArea(TextArea):
    def __init__(self):
        super(SourceViewArea, self).__init__()
        self._language_manager = GtkSource.LanguageManager.get_default()

    def create_buffer(self):
        text_buffer = GtkSource.Buffer()
        return text_buffer

    def create_view(self):
        view = GtkSource.View()
        return view

    def add_from_file(self, filename):
        super(SourceViewArea, self).add_from_file(filename)
        if filename.endswith('.py'):
            self.text_buffer.set_language(
                self._language_manager.get_language('python'))


class App:
    def __init__(self, filename):
        self.filename = filename
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

        self.left_box = St.BoxLayout(style_class="left_box", vertical=True)
        background.add_child(self.left_box)

        self.right_box = St.BoxLayout(style_class="right_box", vertical=True)
        background.add_child(self.right_box)

        self.clutter.show()

        if self.filename:
            self.open_file(self.filename)

    def open_file(self, filename):
        source_view = SourceViewArea()
        source_view.add_from_file(filename)
        self.left_box.add_child(source_view, expand=True)

        v = analyze.analyze(source_view.get_content())
        for reference in v.references.values():
            if not reference.value:
                continue
            doc = reference.value.__doc__
            if not doc:
                continue

            info_ = TextArea()
            info_.set_content(doc.encode('utf-8'))
            self.right_box.add_child(info_, expand=True)

        source_view.grab_focus()

    def on_key_press_event(self, window, event):
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()
            return True
        return False

    def on_window_state_event(self, window, flags):
        state = window.get_window().get_state()
        if state & Gdk.WindowState.FULLSCREEN:
            self.setup_boxes()

def main(args):
    GtkClutter.init([])
    if len(args) > 1:
        filename = args[1]
    else:
        filename = None
    app = App(filename=filename)
    Gtk.main()

sys.exit(main(sys.argv))
