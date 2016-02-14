#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# <from numbers to letters.>
#
# Copyright (C) 2011,2012 Lorenzo Carbonell
# lorenzo.carbonell.cerezo@gmail.com
# Dario Villar <dario.villar.v@gmail.com>
#
# Incluye la modificación de los decimales para que cuando haya cero,
# aparezca reflejado
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
from gi.repository import Gtk, Gdk, GdkPixbuf
from comun import ICON
from comun import VERSION, APPNAME

__author__ = "Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>"
__date__ = "$29-ene-2011$"

# ICON = GdkPixbuf.Pixbuf.new_from_file(
#         '/home/atareao/Dropbox/tp/numerame/media/numerame.svg')

unidades = []
decenas = []
centenas = []
unidades.append('cero')
unidades.append('uno')
unidades.append('dos')
unidades.append('tres')
unidades.append('cuatro')
unidades.append('cinco')
unidades.append('seis')
unidades.append('siete')
unidades.append('ocho')
unidades.append('nueve')
unidades.append('diez')
unidades.append('once')
unidades.append('doce')
unidades.append('trece')
unidades.append('catorce')
unidades.append('quince')
unidades.append('dieciseis')
unidades.append('diecisiete')
unidades.append('dieciocho')
unidades.append('diecinueve')
unidades.append('veinte')
unidades.append('veintiuno')
unidades.append('veintidos')
unidades.append('veintitres')
unidades.append('veinticuatro')
unidades.append('veinticinco')
unidades.append('veintiseis')
unidades.append('veintisiete')
unidades.append('veintiocho')
unidades.append('veintinueve')
unidades.append('treinta')
decenas.append('')
decenas.append('')
decenas.append('')
decenas.append('')
decenas.append('cuarenta')
decenas.append('cincuenta')
decenas.append('sesenta')
decenas.append('setenta')
decenas.append('ochenta')
decenas.append('noventa')
centenas.append('')
centenas.append('ciento')
centenas.append('doscientos')
centenas.append('trescientos')
centenas.append('cuatrocientos')
centenas.append('quinientos')
centenas.append('seiscientos')
centenas.append('setecientos')
centenas.append('ochocientos')
centenas.append('novecientos')

unidadesf = []
decenasf = []
centenasf = []
unidadesf.append('cero')
unidadesf.append('una')
unidadesf.append('dos')
unidadesf.append('tres')
unidadesf.append('cuatro')
unidadesf.append('cinco')
unidadesf.append('seis')
unidadesf.append('siete')
unidadesf.append('ocho')
unidadesf.append('nueve')
unidadesf.append('diez')
unidadesf.append('once')
unidadesf.append('doce')
unidadesf.append('trece')
unidadesf.append('catorce')
unidadesf.append('quince')
unidadesf.append('dieciseis')
unidadesf.append('diecisiete')
unidadesf.append('dieciocho')
unidadesf.append('diecinueve')
unidadesf.append('veinte')
unidadesf.append('veintiuna')
unidadesf.append('veintidos')
unidadesf.append('veintitres')
unidadesf.append('veinticuatro')
unidadesf.append('veinticinco')
unidadesf.append('veintiseis')
unidadesf.append('veintisiete')
unidadesf.append('veintiocho')
unidadesf.append('veintinueve')
unidadesf.append('treinta')
decenasf.append('')
decenasf.append('')
decenasf.append('')
decenasf.append('')
decenasf.append('cuarenta')
decenasf.append('cincuenta')
decenasf.append('sesenta')
decenasf.append('setenta')
decenasf.append('ochenta')
decenasf.append('noventa')
centenasf.append('')
centenasf.append('ciento')
centenasf.append('doscientas')
centenasf.append('trescientas')
centenasf.append('cuatrocientas')
centenasf.append('quinientas')
centenasf.append('seiscientas')
centenasf.append('setecientas')
centenasf.append('ochocientas')
centenasf.append('novecientas')


def is_integer(number):
    try:
        int(number)
        return True
    except:
        return False
    return False


def lee_numero(number):
    if not is_integer(number):
        return ''
    intue = int(number)
    number = str(number)
    longit = len(number)
    if longit < 3:
        if intue < 31:
            numero_leido = unidades[intue]
        elif intue >= 31 and intue <= 39:
            numero_leido = unidades[30] + ' y ' + unidades[intue - 30]
        elif intue == 40:
            numero_leido = decenas[4]
        elif intue >= 41 and intue <= 49:
            numero_leido = decenas[4] + ' y ' + unidades[intue - 40]
        elif intue == 50:
            numero_leido = decenas[5]
        elif intue >= 51 and intue <= 59:
            numero_leido = decenas[5] + ' y ' + unidades[intue - 50]
        elif intue == 60:
            numero_leido = decenas[6]
        elif intue >= 61 and intue <= 69:
            numero_leido = decenas[6] + ' y ' + unidades[intue - 60]
        elif intue == 70:
            numero_leido = decenas[7]
        elif intue >= 71 and intue <= 79:
            numero_leido = decenas[7] + ' y ' + unidades[intue - 70]
        elif intue == 80:
            numero_leido = decenas[8]
        elif intue >= 81 and intue <= 89:
            numero_leido = decenas[8] + ' y ' + unidades[intue - 80]
        elif intue == 90:
            numero_leido = decenas[9]
        elif intue >= 91 and intue <= 99:
            numero_leido = decenas[9] + ' y ' + unidades[intue - 90]
    elif longit < 4:
        parte_izquierda = number[:1]  # number, 1)
        parte_derecha = number[-2:]  # Right(number, 2)
        if parte_derecha == '00' and parte_izquierda == '1':
            numero_leido = 'cien'
        else:
            numero_leido = centenas[
                int(parte_izquierda)] + ' ' + lee_numero(parte_derecha)
    elif longit < 7:
        parte_izquierda = number[:longit - 3]  # Left(number, longit - 3)
        parte_derecha = number[-3:]  # Right(number, 3)
        if int(parte_izquierda) == 0:
            numero_leido = lee_numero(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'mil ' + lee_numero(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numero(
                parte_izquierda) + ' mil ' + lee_numero(parte_derecha)
    elif longit < 13:
        parte_izquierda = number[:longit - 6]  # Left(number, longit - 6)
        parte_derecha = number[-6:]  # Right(number, 6)
        if int(parte_izquierda) == 0:
            numero_leido = lee_numero(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un millón ' + lee_numero(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numero(
                parte_izquierda) + ' millones ' + lee_numero(parte_derecha)
    elif longit < 25:
        parte_izquierda = number[:longit - 12]  # Left(number, longit - 12)
        parte_derecha = number[-12:]  # Right(number, 12)
        if int(parte_izquierda) == 0:
            numero_leido = lee_numero(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un billón ' + lee_numero(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numero(
                parte_izquierda) + ' billones ' + lee_numero(parte_derecha)
    elif longit < 49:
        parte_izquierda = number[:longit - 24]  # Left(number, longit - 24)
        parte_derecha = number[-24:]  # Right(number, 24)
        if int(parte_izquierda) == 0:
            numero_leido = lee_numero(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un trillón ' + lee_numero(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numero(
                parte_izquierda) + ' trillones ' + lee_numero(parte_derecha)
    elif longit < 97:
        parte_izquierda = number[:longit - 48]  # Left(number, longit - 48)
        parte_derecha = number[-48:]  # Right(number, 48)
        if int(parte_izquierda) == 0:
            numero_leido = lee_numero(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un cuatrillón ' + lee_numero(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numero(
                parte_izquierda) + ' cuatrillones ' + lee_numero(parte_derecha)
    elif longit < 193:
        parte_izquierda = number[: longit - 96]  # Left(number, longit - 96)
        parte_derecha = number[- 96:]
        if int(parte_izquierda) == 0:
            numero_leido = lee_numero(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un quintillón ' + lee_numero(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numero(parte_izquierda) + ' quintillones ' +\
                lee_numero(parte_derecha)
    return numero_leido.upper()[:1] + numero_leido.lower()[1:]


def lee_numerof(number):
    if not is_integer(number):
        return ''
    intue = int(number)
    number = str(number)
    longit = len(number)
    if longit < 3:
        if intue < 31:
            numero_leido = unidadesf[intue]
        elif intue >= 31 and intue <= 39:
            numero_leido = unidadesf[30] + ' y ' + unidadesf[intue - 30]
        elif intue == 40:
            numero_leido = decenasf[4]
        elif intue >= 41 and intue <= 49:
            numero_leido = decenasf[4] + ' y ' + unidadesf[intue - 40]
        elif intue == 50:
            numero_leido = decenasf[5]
        elif intue >= 51 and intue <= 59:
            numero_leido = decenasf[5] + ' y ' + unidadesf[intue - 50]
        elif intue == 60:
            numero_leido = decenasf[6]
        elif intue >= 61 and intue <= 69:
            numero_leido = decenasf[6] + ' y ' + unidadesf[intue - 60]
        elif intue == 70:
            numero_leido = decenasf[7]
        elif intue >= 71 and intue <= 79:
            numero_leido = decenasf[7] + ' y ' + unidadesf[intue - 70]
        elif intue == 80:
            numero_leido = decenasf[8]
        elif intue >= 81 and intue <= 89:
            numero_leido = decenasf[8] + ' y ' + unidadesf[intue - 80]
        elif intue == 90:
            numero_leido = decenasf[9]
        elif intue >= 91 and intue <= 99:
            numero_leido = decenasf[9] + ' y ' + unidadesf[intue - 90]
    elif longit < 4:
        parte_izquierda = number[:1]
        parte_derecha = number[-2:]
        if parte_derecha == '00' and parte_izquierda == '1':
            numero_leido = 'cien'
        else:
            numero_leido = centenasf[int(parte_izquierda)] + ' ' +\
                lee_numerof(parte_derecha)
    elif longit < 7:
        parte_izquierda = number[:longit - 3]
        parte_derecha = number[-3:]
        if int(parte_izquierda) == 0:
            numero_leido = lee_numerof(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'mil ' + lee_numerof(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numerof(parte_izquierda) + ' mil ' +\
                lee_numerof(parte_derecha)
    elif longit < 13:
        parte_izquierda = number[:longit - 6]
        parte_derecha = number[-6:]
        if int(parte_izquierda) == 0:
            numero_leido = lee_numerof(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un millón ' + lee_numerof(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numerof(parte_izquierda) + ' millones ' +\
                lee_numerof(parte_derecha)
    elif longit < 25:
        parte_izquierda = number[:longit - 12]
        parte_derecha = number[-12:]
        if int(parte_izquierda) == 0:
            numero_leido = lee_numerof(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un billón ' + lee_numerof(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numerof(parte_izquierda) + ' billones ' +\
                lee_numerof(parte_derecha)
    elif longit < 49:
        parte_izquierda = number[:longit - 24]
        parte_derecha = number[-24:]
        if int(parte_izquierda) == 0:
            numero_leido = lee_numerof(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un trillón ' + lee_numerof(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numerof(parte_izquierda) + ' trillones ' +\
                lee_numerof(parte_derecha)
    elif longit < 97:
        parte_izquierda = number[:longit - 48]
        parte_derecha = number[-48:]
        if int(parte_izquierda) == 0:
            numero_leido = lee_numerof(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un cuatrillón ' + lee_numerof(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numerof(parte_izquierda) + ' cuatrillones ' +\
                lee_numerof(parte_derecha)
    elif longit < 193:
        parte_izquierda = number[:longit - 96]
        parte_derecha = number[-96:]
        if int(parte_izquierda) == 0:
            numero_leido = lee_numerof(parte_derecha)
        elif int(parte_izquierda) == 1:
            numero_leido = 'un quintillón ' + lee_numerof(parte_derecha)
        elif int(parte_izquierda) > 1:
            numero_leido = lee_numerof(parte_izquierda) +\
                ' quintillones ' + lee_numerof(parte_derecha)
    return numero_leido.upper()[:1] + numero_leido.lower()[1:]


class CM(Gtk.Dialog):

    def __init__(self, busqueda_inicial=None):
        Gtk.Dialog.__init__(self, 'numerame', None,
                            Gtk.DialogFlags.MODAL |
                            Gtk.DialogFlags.DESTROY_WITH_PARENT,
                            (Gtk.STOCK_OK, Gtk.ResponseType.ACCEPT))
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_size_request(300, 225)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon(GdkPixbuf.Pixbuf.new_from_file(ICON))
        self.connect('destroy', self.on_close_dialog)
        #
        self.vbox1 = Gtk.VBox(spacing=5)
        self.vbox1.set_border_width(5)
        self.get_content_area().add(self.vbox1)
        #
        self.hbox0 = Gtk.HBox(spacing=5)
        self.hbox0.set_border_width(5)
        self.vbox1.add(self.hbox0)
        #
        self.checkbox = Gtk.CheckButton('Femenino')
        self.checkbox.connect('toggled', self.numera)
        self.hbox0.pack_start(self.checkbox, False, True, 0)
        self.button0 = Gtk.Button('?')
        self.button0.connect('clicked', self.menu_about_response)
        self.hbox0.pack_end(self.button0, False, True, 0)
        #
        self.hbox1 = Gtk.HBox(spacing=5)
        self.hbox1.set_border_width(5)
        self.vbox1.add(self.hbox1)
        #
        self.label = Gtk.Label(fi2u('Número:'))
        self.hbox1.pack_start(self.label, False, False, 0)
        #
        self.entry = Gtk.Entry()
        self.entry.connect("activate", self.numera)
        self.entry.connect('changed', self.numera)
        self.hbox1.pack_start(self.entry, True, True, 0)
        #
        self.frame0 = Gtk.Frame()
        self.vbox1.pack_start(self.frame0, True, True, 0)
        #
        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_size_request(200, 180)
        self.scrolledwindow.set_border_width(2)
        self.frame0.add(self.scrolledwindow)
        self.textview = Gtk.TextView()
        self.scrolledwindow.add(self.textview)
        #
        self.show_all()
        self.set_focus(self.entry)

    def on_close_dialog(self, widget, event, data=None):
        exit(0)

    def menu_about_response(self, widget):
        ad = Gtk.AboutDialog()
        ad.set_name(APPNAME)
        ad.set_version(VERSION)
        ad.set_copyright('Copyrignt (c) 2011-2016\nLorenzo Carbonell')
        ad.set_comments('Una aplicación para pasar de números a letras')
        ad.set_license('''
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
''')
        ad.set_website('http://www.atareao.es')
        ad.set_website_label('http://www.atareao.es')
        ad.set_authors([
            'Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>'])
        ad.set_documenters([
            'Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>'])
        ad.set_logo(GdkPixbuf.Pixbuf.new_from_file(ICON))
        ad.set_icon(GdkPixbuf.Pixbuf.new_from_file(ICON))
        ad.set_program_name(APPNAME)
        ad.run()
        ad.hide()

    def numera(self, widget):
        number = ''
        base = self.entry.get_text()
        base = base.replace('.', ',')
        if base.find(',') != -1:
            entero = base.split(',')
            if len(entero[1]) > 0:
                number = lee_numero(entero[0]) + ' con '
                while(len(entero[1]) > 0 and entero[1][0] == '0'):
                    '''
                    la cadena de decimales es la que habí­a quitando el primer
                    cero ya que ya fue anadido a la cadena number
                    '''
                    entero[1] = (entero[1])[1:len(entero[1])]
                    number = number + 'cero '
                if len(entero[1]) > 0:
                    if self.checkbox.get_active():
                        number = number + lee_numerof(entero[1]).lower()
                    else:
                        number = number + lee_numero(entero[1]).lower()
            else:
                if self.checkbox.get_active():
                    number = lee_numerof(entero[0])
                else:
                    number = lee_numero(entero[0])
        else:
            if self.checkbox.get_active():
                number = lee_numerof(self.entry.get_text())
            else:
                number = lee_numero(self.entry.get_text())
        number = fi2u(number)
        #
        atom = Gdk.atom_intern('CLIPBOARD', True)
        clipboard = self.textview.get_clipboard(atom)
        clipboard.set_text(number, -1)
        #
        ttbuffer = Gtk.TextBuffer()
        ttbuffer.set_text(number)
        self.textview.set_buffer(ttbuffer)
        self.textview.set_editable(False)
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        if number == '':
            self.entry.set_text('')

    def on_exit_activate(self, widget):
        exit(0)


def fi2u(text):
    return text


#   return (text.decode('iso-8859-1')).encode('utf-8')
if __name__ == "__main__":
    '''
    print lee_numero(0)
    print lee_numero(1)
    print lee_numero(12)
    print lee_numero(123)
    print lee_numero(1234)
    print lee_numero(12345)
    print lee_numero(1234567)
    print lee_numero(12345678)
    print lee_numero(123456789)
    print lee_numero(1234567890)
    print lee_numero(12345678901)
    print lee_numero(123456789012)
    '''
    cm = CM()
    cm.run()
    exit(0)
