__author__ = 'aferreiradominguez'

from gi.repository import Gtk

class Cartas(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="Cartas cartas cartas")
        self.set_border_width(10)

        caixa_v=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
        self.add(caixa_v)

        stack=Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        btn_check=Gtk.CheckButton("TouchMe!!")
        stack.add_titled(btn_check,"Push","CheckButtom")

        etiquta=Gtk.Label()
        etiquta.set_markup("<big> BIGLABEL</big>")
        stack.add_titled(etiquta,"Label","BIGLABEL")

        commutador_stack=Gtk.StackSwitcher()
        commutador_stack.set_stack(stack)
        caixa_v.pack_start(commutador_stack,True,True,0)
        caixa_v.pack_start(stack,True,True,0)

carta=Cartas()
carta.connect("delete-event",Gtk.main_quit)
carta.show_all()
Gtk.main()