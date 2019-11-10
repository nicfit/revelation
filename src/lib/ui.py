from __future__ import absolute_import
#
# Revelation - a password manager for GNOME 2
# http://oss.codepoet.no/revelation/
# $Id$
#
# Module for UI functionality
#
#
# Copyright (c) 2003-2006 Erik Grinaker
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from . import config, data, dialog, entry, io, util

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, Gdk, Pango

import gettext, os, pwd, time

_ = gettext.gettext


STOCK_CONTINUE			= "revelation-continue"
STOCK_DISCARD			= "revelation-discard"
STOCK_EDIT			= "revelation-edit"
STOCK_EXPORT			= "revelation-export"
STOCK_FOLDER			= "revelation-folder"
STOCK_GENERATE			= "revelation-generate"
STOCK_IMPORT			= "revelation-import"
STOCK_GOTO			= "revelation-goto"
STOCK_LOCK			= "revelation-lock"
STOCK_NEW_ENTRY			= "revelation-new-entry"
STOCK_NEW_FOLDER		= "revelation-new-folder"
STOCK_NEXT			= "revelation-next"
STOCK_PASSWORD_CHANGE		= "revelation-password-change"
STOCK_PASSWORD_CHECK		= "revelation-password-check"
STOCK_PASSWORD_STRONG		= "revelation-password-strong"
STOCK_PASSWORD_WEAK		= "revelation-password-weak"
STOCK_PREVIOUS			= "revelation-previous"
STOCK_RELOAD			= "revelation-reload"
STOCK_REMOVE			= "revelation-remove"
STOCK_REPLACE			= "revelation-replace"
STOCK_UNKNOWN			= "revelation-unknown"
STOCK_UNLOCK			= "revelation-unlock"
STOCK_UPDATE			= "revelation-update"
STOCK_WARNING			= "revelation-warning"


STOCK_ENTRY_FOLDER		= "revelation-account-folder"
STOCK_ENTRY_FOLDER_OPEN		= "revelation-account-folder-open"
STOCK_ENTRY_CREDITCARD		= "revelation-account-creditcard"
STOCK_ENTRY_CRYPTOKEY		= "revelation-account-cryptokey"
STOCK_ENTRY_DATABASE		= "revelation-account-database"
STOCK_ENTRY_DOOR		= "revelation-account-door"
STOCK_ENTRY_EMAIL		= "revelation-account-email"
STOCK_ENTRY_FTP			= "revelation-account-ftp"
STOCK_ENTRY_GENERIC		= "revelation-account-generic"
STOCK_ENTRY_PHONE		= "revelation-account-phone"
STOCK_ENTRY_SHELL		= "revelation-account-shell"
STOCK_ENTRY_REMOTEDESKTOP		= "revelation-account-remotedesktop"
STOCK_ENTRY_WEBSITE		= "revelation-account-website"

STOCK_REVELATION		= "revelation-revelation"
STOCK_REVELATION_LOCKED		= "revelation-revelation-locked"


ICON_SIZE_APPLET		= Gtk.IconSize.LARGE_TOOLBAR
ICON_SIZE_DATAVIEW		= Gtk.IconSize.LARGE_TOOLBAR
ICON_SIZE_DROPDOWN		= Gtk.IconSize.SMALL_TOOLBAR
ICON_SIZE_ENTRY			= Gtk.IconSize.MENU
ICON_SIZE_FALLBACK		= Gtk.IconSize.LARGE_TOOLBAR
ICON_SIZE_HEADLINE		= Gtk.IconSize.LARGE_TOOLBAR
ICON_SIZE_LABEL			= Gtk.IconSize.MENU
ICON_SIZE_LOGO			= Gtk.IconSize.DND
ICON_SIZE_TREEVIEW		= Gtk.IconSize.MENU

STOCK_ICONS			= (
	( STOCK_REVELATION,		"revelation",			( ICON_SIZE_APPLET, ICON_SIZE_LOGO, Gtk.IconSize.DIALOG, Gtk.IconSize.MENU )),
	( STOCK_REVELATION_LOCKED,	"revelation-locked",		( ICON_SIZE_APPLET, ICON_SIZE_LOGO, Gtk.IconSize.DIALOG, Gtk.IconSize.MENU )),
	( STOCK_ENTRY_CREDITCARD,	"contact-new",			( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_CRYPTOKEY,	"dialog-password",		( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_DATABASE,		"package_system",		( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_DOOR,		"changes-allow",		( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_EMAIL,		"emblem-mail",			( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_FTP,		"system-file-manager",		( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_GENERIC,		"document-new",			( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_PHONE,		"phone",			( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_SHELL,		"utilities-terminal",		( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_REMOTEDESKTOP,	"preferences-desktop-remote-desktop",	( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_WEBSITE,		"web-browser",			( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_FOLDER,		"folder",			( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
	( STOCK_ENTRY_FOLDER_OPEN,	"folder-open",			( ICON_SIZE_DATAVIEW, ICON_SIZE_DROPDOWN, ICON_SIZE_ENTRY, ICON_SIZE_TREEVIEW )),
)

STOCK_ITEMS = (
	( STOCK_CONTINUE,		_('_Continue'),			"stock_test-mode" ),
	( STOCK_DISCARD,		_('_Discard'),			Gtk.STOCK_DELETE ),
	( STOCK_EDIT,			_('_Edit'),			Gtk.STOCK_EDIT ),
	( STOCK_EXPORT,			_('_Export'),			Gtk.STOCK_EXECUTE ),
	( STOCK_FOLDER,			'',				"stock_folder" ),
	( STOCK_GENERATE,		_('_Generate'),			Gtk.STOCK_EXECUTE ),
	( STOCK_GOTO,			_('_Go to'),			Gtk.STOCK_JUMP_TO ),
	( STOCK_IMPORT,			_('_Import'),			Gtk.STOCK_CONVERT ),
	( STOCK_LOCK,			_('_Lock'),			"stock_lock" ),
	( STOCK_NEW_ENTRY,		_('_Add Entry'),		Gtk.STOCK_ADD ),
	( STOCK_NEW_FOLDER,		_('_Add Folder'),		"stock_folder" ),
	( STOCK_NEXT,			_('Next'),			Gtk.STOCK_GO_DOWN ),
	( STOCK_PASSWORD_CHANGE,	_('_Change'),			"stock_lock-ok" ),
	( STOCK_PASSWORD_CHECK,		_('_Check'),			"stock_lock-ok" ),
	( STOCK_PASSWORD_STRONG,	'',				"stock_lock-ok" ),
	( STOCK_PASSWORD_WEAK,		'',				"stock_lock-broken" ),
	( STOCK_PREVIOUS,		_('Previous'),			Gtk.STOCK_GO_UP ),
	( STOCK_RELOAD,			_('_Reload'),			Gtk.STOCK_REFRESH ),
	( STOCK_REMOVE,			_('Re_move'),			Gtk.STOCK_DELETE ),
	( STOCK_REPLACE,		_('_Replace'),			Gtk.STOCK_SAVE_AS ),
	( STOCK_UNKNOWN,		_('Unknown'),			Gtk.STOCK_DIALOG_QUESTION ),
	( STOCK_UNLOCK,			_('_Unlock'),			"stock_lock-open" ),
	( STOCK_UPDATE,			_('_Update'),			"stock_edit" ),
	( STOCK_WARNING,		'',				"stock_dialog-warning" ),
)



##### EXCEPTIONS #####

class DataError(Exception):
	"Exception for invalid data"
	pass



##### FUNCTIONS #####

def config_bind(cfg, key, widget, data = None):
	"Binds a config key to a UI widget"

	if isinstance(widget, Gtk.RadioButton):
		signal	= "toggled"

		def cb_get(config, value, widget):
			if value == data:
				widget.set_active(True)

		def cb_set(widget, key):
			if widget.get_active() == True:
				cfg.set(key, data)


	elif isinstance(widget, Gtk.CheckMenuItem) or isinstance(widget, Gtk.ToggleButton):
		signal	= "toggled"
		cb_get	= lambda c,v,w:	w.set_active(v)
		cb_set	= lambda w,k:	cfg.set(k, w.get_active())

	elif isinstance(widget, Gtk.SpinButton):
		signal	= "changed"
		cb_get	= lambda c,v,w:	w.set_value(v)
		cb_set	= lambda w,k:	cfg.set(k, w.get_value())

	elif isinstance(widget, Gtk.Entry) or isinstance(widget, FileEntry):
		signal	= "changed"
		cb_get	= lambda c,v,w:	w.set_text(v)
		cb_set	= lambda w,k:	cfg.set(k, w.get_text())

	elif isinstance(widget, Gtk.FileChooserButton):
		signal	= "selection-changed"
		cb_get	= lambda c,v,w: w.set_filename(io.file_normpath(v))
		cb_set	= lambda w,k:	cfg.set(k, io.file_normpath(w.get_filename()))

	else:
		raise config.ConfigError

	id = cfg.monitor(key, cb_get, widget)
	widget.connect(signal, cb_set, key)
	widget.connect("destroy", lambda w,i: cfg.forget(i), id)

	return id


def generate_field_display_widget(field, cfg = None, userdata = None):
	"Generates a widget for displaying a field value"

	if field.datatype == entry.DATATYPE_EMAIL:
		widget = LinkButton("mailto:%s" % field.value, util.escape_markup(field.value))

	elif field.datatype == entry.DATATYPE_PASSWORD:
		widget = PasswordLabel(util.escape_markup(field.value), cfg, userdata)

	elif field.datatype == entry.DATATYPE_URL:
		widget = LinkButton(field.value, util.escape_markup(field.value))

	else:
		widget = Label(util.escape_markup(field.value))
		widget.set_selectable(True)

	return widget


def generate_field_edit_widget(field, cfg = None, userdata = None):
	"Generates a widget for editing a field"

	if type(field) == entry.PasswordField:
		widget = PasswordEntryGenerate(None, cfg, userdata)

	elif type(field) == entry.UsernameField:
		widget = ComboBoxEntry(userdata)

	elif field.datatype == entry.DATATYPE_FILE:
		widget = FileEntry()

	elif field.datatype == entry.DATATYPE_PASSWORD:
		widget = PasswordEntry(None, cfg, userdata)

	else:
		widget = Entry()

	widget.set_text(field.value)

	return widget



##### CONTAINERS #####

class Alignment(Gtk.Alignment):
	"A container bin"

	def __init__(self, widget = None, xalign = 0, yalign = 0, xscale = 0, yscale = 0):
		Gtk.Alignment.__init__(self)
		self.set(xalign, yalign, xscale, yscale)

		if widget != None:
			self.add(widget)



class HBox(Gtk.HBox):
	"A horizontal container"

	def __init__(self, *args):
		GObject.Object.__init__(self)

		self.set_spacing(6)
		self.set_border_width(0)

		for widget in args:
			self.pack_start(widget, True, True, 0)




class HButtonBox(Gtk.HButtonBox):
	"A horizontal button box"

	def __init__(self, *args):
		GObject.Object.__init__(self)

		self.set_layout(Gtk.ButtonBoxStyle.SPREAD)
		self.set_spacing(12)

		for button in args:
			self.pack_start(button, True, True, 0)



class VBox(Gtk.VBox):
	"A vertical container"

	def __init__(self, *args):
		GObject.Object.__init__(self)

		self.set_spacing(6)
		self.set_border_width(0)

		for widget in args:
			self.pack_start(widget, False, False, 0)



class HPaned(Gtk.HPaned):
	"A horizontal pane"

	def __init__(self, left = None, right = None):
		GObject.Object.__init__(self)
		self.set_border_width(6)

		if left is not None:
			self.pack1(left, True, True)

		if right is not None:
			self.pack2(right, True, True)



class Notebook(Gtk.Notebook):
	"A notebook (tabbed view)"

	def __init__(self):
		GObject.Object.__init__(self)


	def create_page(self, title):
		"Creates a notebook page"

		page = NotebookPage()
		self.append_page(page, Label(title))

		return page



class NotebookPage(VBox):
	"A notebook page"

	def __init__(self):
		VBox.__init__(self)

		self.sizegroup = Gtk.SizeGroup(Gtk.SizeGroupMode.HORIZONTAL)
		self.set_border_width(12)
		self.set_spacing(18)


	def add_section(self, title, description = None):
		"Adds an input section to the notebook"

		section = InputSection(title, description, self.sizegroup)
		self.pack_start(section, False, False, 0)

		return section



class ScrolledWindow(Gtk.ScrolledWindow):
	"A scrolled window for partially displaying a child widget"

	def __init__(self, contents = None):
		GObject.Object.__init__(self)

		self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

		if contents is not None:
			self.add(contents)



class Table(Gtk.Table):
	"A table"

	def __init__(self, rows = 1, cols = 1, homogenous = False):
		Gtk.Table.__init__(self, rows, cols, homogenous)

		self.set_row_spacings(3)
		self.set_col_spacings(6)


	def attach(self, widget, x, y, colspan = 1, rowspan = 1, xoptions = Gtk.AttachOptions.FILL, yoptions = 0):
		"Attaches a widget to the table"

		Gtk.Table.attach(self, widget, x, x + colspan, y, y + colspan, xoptions, yoptions)



class Toolbar(Gtk.Toolbar):
	"A Toolbar subclass"

	def append_space(self):
		"Appends a space to the toolbar"

		space = Gtk.SeparatorToolItem()
		space.set_draw(False)

		self.insert(space, -1)


	def append_widget(self, widget, tooltip = None):
		"Appends a widget to the toolbar"

		toolitem = Gtk.ToolItem()
		toolitem.add(widget)

		if tooltip != None:
			toolitem.set_tooltip_text(tooltip)

		self.insert(toolitem, -1)



class InputSection(VBox):
	"A section of input fields"

	def __init__(self, title = None, description = None, sizegroup = None):
		VBox.__init__(self)

		self.title	= None
		self.desc	= None
		self.sizegroup	= sizegroup

		if title is not None:
			self.title = Label("<span weight=\"bold\">%s</span>" % util.escape_markup(title))
			# FIXME: port
			self.pack_start(self.title, False, False, 0)

		if description is not None:
			self.desc = Label(util.escape_markup(description))
			# FIXME: port
			self.pack_start(self.desc, False, False, 0)

		if sizegroup is None:
			self.sizegroup = Gtk.SizeGroup(Gtk.SizeGroupMode.HORIZONTAL)


	def append_widget(self, title, widget, indent = True):
		"Adds a widget to the section"

		row = HBox()
		row.set_spacing(12)
		self.pack_start(row, False, False, 0)

		if self.title is not None and indent == True:
			l = Label("", True)
			row.pack_start(l, False, False, 0)

		if title is not None:
			label = Label("%s:" % util.escape_markup(title))
			self.sizegroup.add_widget(label)
			row.pack_start(label, False, False, 0)

		row.pack_start(widget, True, False, 0)


	def clear(self):
		"Removes all widgets"

		for child in self.get_children():
			if child not in ( self.title, self.desc ):
				child.destroy()



##### DISPLAY WIDGETS #####

class EventBox(Gtk.EventBox):
	"A container which handles events for a widget (for tooltips etc)"

	def __init__(self, widget = None):
		GObject.Object.__init__(self)

		# FIXME: port
		# self.widget = widget

		if widget is not None:
			# FIXME: port
			# self.add(self.widget)
			self.add(widget)



class Image(Gtk.Image):
	"A widget for displaying an image"

	def __init__(self, stock = None, size = None):
		GObject.GObject.__init__(self)

		if stock is not None:
			self.set_from_stock(stock, size)



class ImageLabel(HBox):
	"A label with an image"

	def __init__(self, text = None, stock = None, size = ICON_SIZE_LABEL):
		HBox.__init__(self)

		self.image = Image()
		self.pack_start(self.image, False, True, 0)

		self.label = Label(text)
		self.pack_start(self.label, True, True, 0)

		if text != None:
			self.set_text(text)

		if stock != None:
			self.set_stock(stock, size)


	def set_ellipsize(self, ellipsize):
		"Sets label ellisization"

		self.label.set_ellipsize(ellipsize)


	def set_stock(self, stock, size):
		"Sets the image"

		self.image.set_from_stock(stock, size)


	def set_text(self, text):
		"Sets the label text"

		self.label.set_text(text)



class Label(Gtk.Label):
	"A text label"

	def __init__(self, text = None, justify = Gtk.Justification.LEFT):
		GObject.Object.__init__(self)

		self.set_text(text)
		self.set_justify(justify)
		self.set_use_markup(True)
		self.set_line_wrap(True)

		if justify == Gtk.Justification.LEFT:
			self.set_alignment(0, 0.5)

		elif justify == Gtk.Justification.CENTER:
			self.set_alignment(0.5, 0.5)

		elif justify == Gtk.Justification.RIGHT:
			self.set_alignment(1, 0.5)


	def set_text(self, text):
		"Sets the text of the label"

		if text is None:
			Gtk.Label.set_text(self, "")

		else:
			Gtk.Label.set_markup(self, text)



class PasswordLabel(EventBox):
	"A label for displaying passwords"

	def __init__(self, password = "", cfg = None, clipboard = None, justify = Gtk.Justification.LEFT):
		EventBox.__init__(self)

		self.password	= util.unescape_markup(password)
		self.config	= cfg
		self.clipboard	= clipboard

		self.label = Label(util.escape_markup(self.password), justify)
		self.label.set_selectable(True)
		self.add(self.label)

		if self.config is not None:
			try:
				self.config.monitor("view/passwords", lambda k,v,d: self.show_password(v))

			except config.ConfigError:
				self.config.monitor("show_passwords", lambda k,v,d: self.show_password(v))

		self.connect("button-press-event", self.__cb_button_press)
		self.connect("drag-data-get", self.__cb_drag_data_get)


	def __cb_drag_data_get(self, widget, context, selection, info, timestamp, data = None):
		"Provides data for a drag operation"

		selection.set_text(self.password, -1)


	def __cb_button_press(self, widget, data = None):
		"Populates the popup menu"

		if self.label.get_selectable() == True:
			return False

		elif data.button == 3:
			menu = Menu()

			menuitem = ImageMenuItem(Gtk.STOCK_COPY, _('Copy password'))
			menuitem.connect("activate", lambda w: self.clipboard.set(self.password, True))
			menu.append(menuitem)

			menu.show_all()
			menu.popup(None, None, None, data.button, data.time)

			return True


	def set_ellipsize(self, ellipsize):
		"Sets ellipsize for the label"

		self.label.set_ellipsize(ellipsize)


	def show_password(self, show = True):
		"Sets whether to display the password"

		if show == True:
			self.label.set_text(util.escape_markup(self.password))
			self.label.set_selectable(True)
			self.drag_source_unset()

		else:
			self.label.set_text("******")
			self.label.set_selectable(False)

			''' FIXME: port
			self.drag_source_set(
				Gdk.ModifierType.BUTTON1_MASK,
				(
					("text/plain", 0, 0),
					("TEXT", 0, 1),
					("STRING", 0, 2),
					("COMPOUND TEXT", 0, 3),
					("UTF8_STRING", 0, 4),
				),
				Gdk.DragAction.COPY
			)
			'''



class EditableTextView(Gtk.ScrolledWindow):
	"An editable text view"

	def __init__(self, buffer = None, text = None):

		GObject.GObject.__init__(self)
		self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
		self.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
		self.textview = Gtk.TextView()
		self.textview.set_buffer(buffer)
		self.textbuffer = self.textview.get_buffer()
		self.add(self.textview)

		if text is not None:
			self.textview.get_buffer().set_text(text)

	def set_text(self, text):
		"Sets the entry contents"

		if text is None:
			self.textbuffer.set_text("")

		self.textbuffer.set_text(text)

	def get_text(self):
		"Returns the text of the entry"

		return self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter())

class TextView(Gtk.TextView):
	"A text view"

	def __init__(self, buffer = None, text = None):
		Gtk.TextView.__init__(self)
		self.set_buffer(buffer)


		self.set_editable(False)
		self.set_wrap_mode(Gtk.WrapMode.NONE)
		self.set_cursor_visible(False)
		self.modify_font(Pango.FontDescription("Monospace"))

		if text is not None:
			self.get_buffer().set_text(text)



##### TEXT ENTRIES #####

class Entry(Gtk.Entry):
	"A normal text entry"

	def __init__(self, text = None):
		GObject.GObject.__init__(self)

		self.set_activates_default(True)
		self.set_text(text)


	def set_text(self, text):
		"Sets the entry contents"

		if text is None:
			text = ""

		Gtk.Entry.set_text(self, text)



class ComboBoxEntry(Gtk.ComboBox):
	"An entry with a combo box list"

	def __init__(self, list = []):
		GObject.Object.__init__(self)

		self.entry = self.get_child()
		# self.entry.set_activates_default(True)

		self.model = Gtk.ListStore(GObject.TYPE_STRING)
		self.set_model(self.model)
		self.set_entry_text_column(0)

		# FIXME: port
		'''
		self.completion = Gtk.EntryCompletion()
		self.completion.set_model(self.model)
		self.completion.set_text_column(0)
		self.completion.set_minimum_key_length(1)
		self.entry.set_completion(self.completion)
		'''

		if list is not None:
			self.set_values(list)


	def get_text(self):
		"Returns the text of the entry"

		return self.entry.get_text()


	def set_text(self, text):
		"Sets the text of the entry"

		if text is None:
			# FIXME: port
			# self.entry.set_text("")
			return

		# FIXME: port
		print("set_text:", text)
		# self.entry.set_text(text)


	def set_values(self, datalist):
		"Sets the values for the dropdown"

		self.model.clear()

		for item in datalist:
			self.model.append((item,))



class FileEntry(HBox):
	"A file entry"

	def __init__(self, title = None, file = None, type = Gtk.FileChooserAction.OPEN):
		HBox.__init__(self)

		self.title = title is not None and title or _('Select File')
		self.type = type

		self.entry = Entry()
		self.entry.connect("changed", lambda w: self.emit("changed"))
		self.pack_start(self.entry, True, True, 0)

		self.button = Button(_('Browse...'), self.__cb_filesel)
		self.pack_start(self.button, False, False, 0)

		if file is not None:
			self.set_filename(file)


	def __cb_filesel(self, widget, data = None):
		"Displays a file selector when Browse is pressed"

		try:
			fsel = dialog.FileSelector(None, self.title, self.type)
			file = self.get_filename()

			if file != None:
				fsel.set_filename(file)

			self.set_filename(fsel.run())

		except dialog.CancelError:
			pass


	def get_filename(self):
		"Gets the current filename"

		return io.file_normpath(self.entry.get_text())


	def get_text(self):
		"Wrapper to emulate Entry"

		return self.entry.get_text()


	def set_filename(self, filename):
		"Sets the current filename"

		self.entry.set_text(io.file_normpath(filename))
		self.entry.set_position(-1)


	def set_text(self, text):
		"Wrapper to emulate Entry"

		self.entry.set_text(text)


GObject.type_register(FileEntry)
GObject.signal_new("changed", FileEntry, GObject.SignalFlags.ACTION, GObject.TYPE_BOOLEAN, ())



class IconEntry(Alignment):
	"An entry with an icon in it"

	def __init__(self, text = None):
		Alignment.__init__(self)

		self.icon	= None
		self.icontip	= None

		# set up ui
		self.hbox = HBox()
		self.add(self.hbox)

		self.entry = Entry(text)
		self.entry.set_has_frame(False)
		self.hbox.pack_start(self.entry, True, True, 0)

		self.iconebox	= EventBox()
		self.iconebox.set_visible_window(False)

		self.iconalign	= Alignment(self.iconebox, 1.0, 0.5, 0, 0)
		self.iconalign.set_padding(1, 1, 0, 2)

		# connect signals
		# FIXME: port
		self.connect("draw", self.__cb_expose)
		# self.connect("size-allocate", self.__cb_size_allocate)
		# self.connect("size-request", self.__cb_size_request)

		self.entry.connect_after("focus-in-event", lambda w,d: self.queue_draw())
		self.entry.connect_after("focus-out-event", lambda w,d: self.queue_draw())

		self.entry.connect("changed", lambda w: self.emit("changed"))
		self.entry.connect("populate-popup", lambda w,m: self.emit("populate-popup", m))


	def __cb_expose(self, widget, data):
		"Draws the widget borders on expose"

		allocation	= self.get_allocation()
		style		= self.entry.get_style()
		intfocus	= self.entry.style_get_property("interior-focus")
		focuswidth	= self.entry.style_get_property("focus-line-width")

		x		= allocation.x
		y		= allocation.y
		width		= allocation.width
		height		= allocation.height

		# FIXME: port
		# if self.entry.flags() & Gtk.HAS_FOCUS == Gtk.HAS_FOCUS and intfocus == False:
		if intfocus == False:
			x	+= focuswidth
			y	+= focuswidth
			width	-= 2 * focuswidth
			height	-= 2 * focuswidth

		# FIXME: port
		# style.paint_flat_box(self.window, self.entry.state, Gtk.ShadowType.NONE, None, self.entry, "entry_bg", x, y, width, height)
		# style.paint_shadow(self.window, Gtk.StateType.NORMAL, Gtk.ShadowType.IN, None, self.entry, "entry", x, y, width, height)

		# if self.entry.flags() & Gtk.HAS_FOCUS == Gtk.HAS_FOCUS and intfocus == False:
		if intfocus == False:
			x	-= focuswidth
			y	-= focuswidth
			width	+= 2 * focuswidth
			height	+= 2 * focuswidth

			style.paint_focus(self.window, self.entry.state, None, self.entry, "entry", x, y, width, height)


	def __cb_size_allocate(self, widget, allocation):
		"Modifies the widget size allocation"

		child_allocation	= ()
		xborder, yborder	= self.__entry_get_borders()

		child_allocation.x	= allocation.x + self.border_width + xborder
		child_allocation.y	= allocation.y + self.border_width + yborder
		child_allocation.width	= max(allocation.width - (self.border_width + xborder) * 2, 0)
		child_allocation.height	= max(allocation.height - (self.border_width + yborder) * 2, 0)

		self.hbox.size_allocate(child_allocation)
		self.queue_draw()


	def __cb_size_request(self, widget, requisition):
		"Modifies the widget size request"

		requisition.width	= self.border_width * 2
		requisition.height	= self.border_width * 2
		xborder, yborder	= self.__entry_get_borders()

		entrywidth, entryheight	= self.entry.size_request()
		requisition.height	+= entryheight >= 18 and entryheight or 18

		requisition.width	+= 2 * xborder
		requisition.height	+= 2 * yborder


	def __entry_get_borders(self):
		"Returns the border sizes of an entry"

		style		= self.entry.get_style()
		intfocus	= self.entry.style_get_property("interior-focus")
		focuswidth	= self.entry.style_get_property("focus-line-width")

		xborder		= style.xthickness
		yborder		= style.ythickness

		if intfocus == False:
			xborder	+= focuswidth
			yborder	+= focuswidth

		return xborder, yborder


	def get_text(self):
		"Wrapper for the entry"

		return self.entry.get_text()


	def grab_focus(self):
		"Wrapper for Gtk.Entry.grab_focus()"

		return self.entry.grab_focus()


	def remove_icon(self):
		"Removes the icon from the entry"

		self.set_icon(None, "")


	def set_editable(self, editable):
		"Wrapper for Gtk.Entry.set_editable()"

		self.entry.set_editable(editable)


	def set_icon(self, stock, tooltip = ""):
		"Sets the icon for the entry"

		if tooltip != self.icontip:
			self.iconebox.set_tooltip_text(tooltip)
			self.icontip = tooltip

		if self.icon != None and self.icon.get_stock()[0] == stock:
			return

		if self.iconalign in self.hbox.get_children():
			self.hbox.remove(self.iconalign)
			self.iconebox.remove(self.icon)
			self.icon.destroy()
			self.icon = None

		if stock == None:
			return

		self.icon = Image(stock, ICON_SIZE_ENTRY)
		self.iconebox.add(self.icon)
		self.hbox.pack_start(self.iconalign, False, False, 0)
		self.hbox.show_all()


	def set_text(self, text):
		"Wrapper for the entry"

		self.entry.set_text(text)


	def set_width_chars(self, width):
		"Wrapper for Gtk.Entry.set_width_chars"

		self.entry.set_width_chars(width)


	def set_visibility(self, visibility):
		"Wrapper for the entry"

		self.entry.set_visibility(visibility)


GObject.type_register(IconEntry)
GObject.signal_new("changed", IconEntry, GObject.SignalFlags.ACTION, GObject.TYPE_BOOLEAN, ())
GObject.signal_new("populate-popup", IconEntry, GObject.SignalFlags.ACTION, GObject.TYPE_BOOLEAN, (GObject.TYPE_PYOBJECT, ))



class PasswordEntry(IconEntry):
	"An entry for editing a password (follows the 'show passwords' preference)"

	def __init__(self, password = None, cfg = None, clipboard = None):
		IconEntry.__init__(self, password)
		self.set_visibility(False)

		self.autocheck	= True
		self.config	= cfg
		self.clipboard	= clipboard

		self.connect("changed", self.__cb_check_password)
		self.connect("populate-popup", self.__cb_popup)

		if cfg != None:
			self.config.monitor("view/passwords", lambda k,v,d: self.set_visibility(v))


	def __cb_check_password(self, widget, data = None):
		"Callback for changed, checks the password"

		if self.autocheck == False:
			return

		password = self.get_text()

		if len(password) == 0:
			self.remove_icon()

		else:
			try:
				util.check_password(password)

			except ValueError as reason:
				self.set_password_strong(False, _('The password %s') % str(reason))

			else:
				self.set_password_strong(True, _('The password seems good'))


	def __cb_popup(self, widget, menu):
		"Populates the popup menu"

		if self.clipboard != None:
			menuitem = ImageMenuItem(Gtk.STOCK_COPY, _('Copy password'))
			menuitem.connect("activate", lambda w: self.clipboard.set(self.get_text(), True))

			menu.insert(menuitem, 2)

		menu.show_all()


	def set_password_strong(self, strong, reason = ""):
		"Sets whether the password is strong or not"

		self.set_icon(strong == True and STOCK_PASSWORD_STRONG or STOCK_PASSWORD_WEAK, reason)



class PasswordEntryGenerate(HBox):
	"A password entry with a generator button"

	def __init__(self, password = None, cfg = None, clipboard = None):
		HBox.__init__(self)
		self.config = cfg

		self.pwentry = PasswordEntry(password, cfg, clipboard)
		self.pack_start(self.pwentry, True, True, 0)

		self.button = Button(_('Generate'), lambda w: self.generate())
		self.pack_start(self.button, False, False, 0)

		self.entry = self.pwentry.entry


	def generate(self):
		"Generates a password for the entry"

		password = util.generate_password(self.config.get("passwordgen/length"),self.config.get("passwordgen/punctuation"))
		self.pwentry.set_text(password)


	def get_text(self):
		"Wrapper for the entry"

		return self.pwentry.get_text()


	def set_text(self, text):
		"Wrapper for the entry"

		self.pwentry.set_text(text)



class SpinEntry(Gtk.SpinButton):
	"An entry for numbers"

	def __init__(self, adjustment = None, climb_rate = 0.0, digits = 0):
		Gtk.SpinButton.__init__(self)
		self.configure(adjustment, climb_rate, digits)

		self.set_increments(1, 5)
		self.set_range(0, 100000)
		self.set_numeric(True)



##### BUTTONS #####

class Button(Gtk.Button):
	"A normal button"

	def __init__(self, label, callback = None):
		Gtk.Button.__init__(self, label)

		self.set_use_stock(True)

		if callback is not None:
			self.connect("clicked", callback)



class CheckButton(Gtk.CheckButton):
	"A checkbutton"

	def __init__(self, label = None):
		Gtk.CheckButton.__init__(self, label)



class DropDown(Gtk.ComboBox):
	"A dropdown button"

	def __init__(self, icons = False):
		GObject.GObject.__init__(self)

		self.model = Gtk.ListStore(GObject.TYPE_STRING, GObject.TYPE_STRING, GObject.TYPE_PYOBJECT)
		self.set_model(self.model)

		if icons == True:
			cr = Gtk.CellRendererPixbuf()
			cr.set_fixed_size(Gtk.icon_size_lookup(ICON_SIZE_DROPDOWN)[0] + 5, -1)
			self.pack_start(cr, False)
			self.add_attribute(cr, "stock-id", 1)

		cr = Gtk.CellRendererText()
		self.pack_start(cr, True)
		self.add_attribute(cr, "text", 0)

		self.connect("realize", self.__cb_show)


	def __cb_show(self, widget, data = None):
		"Callback for when widget is shown"

		if self.get_active() == -1:
			self.set_active(0)


	def append_item(self, text, stock = None, data = None):
		"Appends an item to the dropdown"

		self.model.append( ( text, stock, data ) )


	def delete_item(self, index):
		"Removes an item from the dropdown"

		if self.model.iter_n_children(None) > index:
			iter = self.model.iter_nth_child(None, index)
			self.model.remove(iter)


	def get_active_item(self):
		"Returns a tuple with data for the current item"

		iter = self.model.iter_nth_child(None, self.get_active())
		return self.model.get(iter, 0, 1, 2)


	def get_item(self, index):
		"Returns data for an item"

		return self.model.get(self.model.iter_nth_child(None, index), 0, 1, 2)


	def get_num_items(self):
		"Returns the number of items in the dropdown"

		return self.model.iter_n_children(None)


	def insert_item(self, index, text, stock = None, data = None):
		"Inserts an item in the dropdown"

		self.model.insert(index, ( text, stock, data ) )



class EntryDropDown(DropDown):
	"An entry type dropdown"

	def __init__(self):
		DropDown.__init__(self, True)

		for e in entry.ENTRYLIST:
			if e != entry.FolderEntry:
				self.append_item(e().typename, e().icon, e)


	def get_active_type(self):
		"Get the currently active type"

		item = self.get_active_item()

		if item is not None:
			return item[2]


	def set_active_type(self, entrytype):
		"Set the active type"

		for i in range(self.model.iter_n_children(None)):
			iter = self.model.iter_nth_child(None, i)

			if self.model.get_value(iter, 2) == entrytype:
				self.set_active(i)


class FileButton(Gtk.FileChooserButton):
	"A file chooser button"

	def __init__(self, title = None, file = None, type = Gtk.FileChooserAction.OPEN):
		Gtk.FileChooserButton.__init__(self, title)
		self.set_action(type)
		self.set_local_only(False)

		if file != None:
			self.set_filename(file)


	def get_filename(self):
		"Gets the filename"

		return io.file_normpath(self.get_uri())


	def set_filename(self, filename):
		"Sets the filename"

		filename = io.file_normpath(filename)

		if filename != io.file_normpath(self.get_filename()):
			Gtk.FileChooserButton.set_filename(self, filename)


class LinkButton(Gtk.LinkButton):
	"A link button"

	def __init__(self, url, label):
		Gtk.LinkButton.__init__(self, url, label)
		self.set_alignment(0, 0.5)

		self.label = self.get_children()[0]

		"If URI is too long reduce it for the label"
		if len(label) > 60:
			self.label.set_text(label[0:59] + " (...)")

	def set_ellipsize(self, ellipsize):
		"Sets ellipsize for label"

		self.label.set_ellipsize(ellipsize)


	def set_justify(self, justify):
		"Sets justify for label"

		self.label.set_justify(justify)


class RadioButton(Gtk.RadioButton):
	"A radio button"

	def __init__(self, group, label):
		Gtk.RadioButton.__init__(self, group=group, label=label)



##### MENUS AND MENU ITEMS #####

class ImageMenuItem(Gtk.ImageMenuItem):
	"A menuitem with a stock icon"

	def __init__(self, stock, text = None):
		Gtk.ImageMenuItem.__init__(self, stock)

		self.label = self.get_children()[0]
		self.image = self.get_image()

		if text is not None:
			self.set_text(text)


	def set_stock(self, stock):
		"Set the stock item to use as icon"

		self.image.set_from_stock(stock, Gtk.IconSize.MENU)


	def set_text(self, text):
		"Set the item text"

		self.label.set_text(text)



class Menu(Gtk.Menu):
	"A menu"

	def __init__(self):
		GObject.GObject.__init__(self)



##### MISCELLANEOUS WIDGETS #####

class TreeView(Gtk.TreeView):
	"A tree display"

	def __init__(self, model):
		Gtk.TreeView.__init__(self, model)
		self.set_headers_visible(False)
		self.model = model

		self.__cbid_drag_motion	= None
		self.__cbid_drag_end	= None

		self.selection = self.get_selection()
		self.selection.set_mode(Gtk.SelectionMode.MULTIPLE)

		self.connect("button_press_event", self.__cb_buttonpress)
		self.connect("key_press_event", self.__cb_keypress)


	def __cb_buttonpress(self, widget, data):
		"Callback for handling mouse clicks"

		path = self.get_path_at_pos(int(data.x), int(data.y))

		# handle click outside entry
		if path is None:
			self.unselect_all()

		# handle doubleclick
		if data.button == 1 and data.type == Gdk.EventType._2BUTTON_PRESS and path != None:
			iter = self.model.get_iter(path[0])
			self.toggle_expanded(iter)

			if iter != None:
				self.emit("doubleclick", iter)

		# display popup on right-click
		elif data.button == 3:
			if path != None and self.selection.iter_is_selected(self.model.get_iter(path[0])) == False:
				self.set_cursor(path[0], path[1], False)

			self.emit("popup", data)

			return True

		# handle drag-and-drop of multiple rows
		elif self.__cbid_drag_motion == None and data.button in ( 1, 2 ) and data.type == Gdk.EventType.BUTTON_PRESS and path != None and self.selection.iter_is_selected(self.model.get_iter(path[0])) == True and len(self.get_selected()) > 1:
			self.__cbid_drag_motion = self.connect("motion_notify_event", self.__cb_drag_motion, data.copy() )
			self.__cbid_drag_end = self.connect("button_release_event", self.__cb_button_release, data.copy() )

			return True


	def __cb_button_release(self, widget, data, userdata = None):
		"Ends a drag"

		self.emit("button_press_event", userdata)
		self.__drag_check_end()


	def __cb_drag_motion(self, widget, data, userdata = None):
		"Monitors drag motion"

		if self.drag_check_threshold(int(userdata.x), int(userdata.y), int(data.x), int(data.y)) == True:
			self.__drag_check_end()
			self.drag_begin( (( "revelation/treerow", Gtk.TargetFlags.SAME_APP | Gtk.TargetFlags.SAME_WIDGET, 0), ), Gdk.DragAction.MOVE, userdata.button, userdata)


	def __cb_keypress(self, widget, data = None):
		"Callback for handling key presses"

		# expand/collapse node on space
		if data.keyval == 32:
			self.toggle_expanded(self.get_active())


	def __drag_check_end(self):
		"Ends a drag check"

		self.disconnect(self.__cbid_drag_motion)
		self.disconnect(self.__cbid_drag_end)

		self.__cbid_drag_motion = None
		self.__cbid_drag_end = None


	def collapse_row(self, iter):
		"Collapse a tree row"

		Gtk.TreeView.collapse_row(self, self.model.get_path(iter))


	def expand_row(self, iter):
		"Expand a tree row"

		if iter is not None and self.model.iter_n_children(iter) > 0:
			Gtk.TreeView.expand_row(self, self.model.get_path(iter), False)


	def expand_to_iter(self, iter):
		"Expand all items up to and including a given iter"

		path = self.model.get_path(iter)

		for i in range(len(path)):
			iter = self.model.get_iter(path[0:i])
			self.expand_row(iter)


	def get_active(self):
		"Get the currently active row"

		if self.model == None:
			return None

		iter = self.model.get_iter(self.get_cursor()[0])

		if iter is None or self.selection.iter_is_selected(iter) == False:
			return None

		return iter

	def get_selected(self):
		"Get a list of currently selected rows"

		list = []
		self.selection.selected_foreach(lambda model, path, iter: list.append(iter))

		return list


	def select(self, iter):
		"Select a particular row"

		if iter == None:
			self.unselect_all()

		else:
			self.expand_to_iter(iter)
			self.set_cursor(self.model.get_path(iter))


	def select_all(self):
		"Select all rows in the tree"

		self.selection.select_all()
		self.selection.emit("changed")
		self.emit("cursor_changed")


	def set_model(self, model):
		"Change the tree model which is being displayed"

		Gtk.TreeView.set_model(self, model)
		self.model = model


	def toggle_expanded(self, iter):
		"Toggle the expanded state of a row"

		if iter is None:
			return

		elif self.row_expanded(self.model.get_path(iter)):
			self.collapse_row(iter)

		else:
			self.expand_row(iter)


	def unselect_all(self):
		"Unselect all rows in the tree"

		self.selection.unselect_all()
		self.selection.emit("changed")
		self.emit("cursor_changed")
		self.emit("unselect_all")


GObject.signal_new("doubleclick", TreeView, GObject.SignalFlags.ACTION, GObject.TYPE_BOOLEAN, (GObject.TYPE_PYOBJECT, ))
GObject.signal_new("popup", TreeView, GObject.SignalFlags.ACTION, GObject.TYPE_BOOLEAN, (GObject.TYPE_PYOBJECT, ))



class EntryTree(TreeView):
	"An entry tree"

	def __init__(self, entrystore):
		TreeView.__init__(self, entrystore)

		column = Gtk.TreeViewColumn()
		self.append_column(column)

		cr = Gtk.CellRendererPixbuf()
		column.pack_start(cr, False) 
		column.add_attribute(cr, "stock-id", data.COLUMN_ICON)
		cr.set_property("stock-size", ICON_SIZE_TREEVIEW)

		cr = Gtk.CellRendererText()
		column.pack_start(cr, True)
		column.add_attribute(cr, "text", data.COLUMN_NAME)

		self.connect("doubleclick", self.__cb_doubleclick)
		self.connect("row-expanded", self.__cb_row_expanded)
		self.connect("row-collapsed", self.__cb_row_collapsed)


	def __cb_doubleclick(self, widget, iter):
		"Stop doubleclick emission on folder"

		if type(self.model.get_entry(iter)) == entry.FolderEntry:
			self.stop_emission("doubleclick")


	def __cb_row_collapsed(self, object, iter, extra):
		"Updates folder icons when collapsed"

		self.model.folder_expanded(iter, False)


	def __cb_row_expanded(self, object, iter, extra):
		"Updates folder icons when expanded"

		# make sure all children are collapsed (some may have lingering expand icons)
		for i in range(self.model.iter_n_children(iter)):
			child = self.model.iter_nth_child(iter, i)

			if self.row_expanded(self.model.get_path(child)) == False:
				self.model.folder_expanded(child, False)

		self.model.folder_expanded(iter, True)


	def set_model(self, model):
		"Sets the model displayed by the tree view"

		TreeView.set_model(self, model)

		if model is None:
			return

		for i in range(model.iter_n_children(None)):
			model.folder_expanded(model.iter_nth_child(None, i), False)



class Statusbar(Gtk.Statusbar):
	"An application statusbar"

	def __init__(self):
		GObject.GObject.__init__(self)
		self.contextid = self.get_context_id("statusbar")


	def clear(self):
		"Clears the statusbar"

		self.pop(self.contextid)


	def set_status(self, text):
		"Displays a text in the statusbar"

		self.clear()
		self.push(self.contextid, text)



##### FACTORIES AND MANAGERS #####

class ItemFactory(Gtk.IconFactory):
	"A stock item factory"

	def __init__(self, parent):
		GObject.GObject.__init__(self)
		self.add_default()

		self.parent	= parent
		self.theme	= Gtk.IconTheme.get_default()

		if config.DIR_ICONS not in self.theme.get_search_path():
			self.theme.append_search_path(config.DIR_ICONS)

		self.__init_icons()
		self.__init_items()

		self.theme.connect("changed", self.__cb_theme_changed)


	def __init_icons(self):
		"Loads stock icons"

		for id, icon, sizes in STOCK_ICONS:
			self.create_stock_icon(id, icon, sizes)


	def __init_items(self):
		"Creates stock items"

		# FIXME: port
		return

		for id, name, icon in STOCK_ITEMS:
			self.create_stock_item(id, name, icon)


	def __cb_theme_changed(self, widget, data = None):
		"Callback for changed theme"

		self.__init_icons()
		self.__init_items()


	def create_stock_icon(self, id, icon, sizes):
		"Creates a stock icon from a different stock icon"

		iconset = Gtk.IconSet()
		self.add(id, iconset)

		if self.theme.has_icon(icon) == False:
			return

		# load icons (the dict.fromkeys() thing is to remove duplicates)
		for size in dict.fromkeys(sizes).keys():
			source = self.get_iconsource(icon, size)

			if source != None:
				iconset.add_source(source)


		# load fallback icon if none were found
		if len(iconset.get_sizes()) == 0:
			source = self.get_iconsource(icon, ICON_SIZE_FALLBACK, True)

			if source != None:
				iconset.add_source(source)


	def create_stock_item(self, id, name, icon = None):
		"Creates a stock item"

		Gtk.stock_add(((id, name, 0, 0, None), ))

		if icon is None:
			pass

		elif Gtk.stock_lookup(icon) is not None:
			self.add(id, self.parent.get_style().lookup_icon_set(icon))

		else:
			self.create_stock_icon(id, icon, ( Gtk.IconSize.SMALL_TOOLBAR, Gtk.IconSize.LARGE_TOOLBAR, Gtk.IconSize.MENU, Gtk.IconSize.BUTTON, Gtk.IconSize.DIALOG, ICON_SIZE_LABEL, ICON_SIZE_HEADLINE ))


	def get_iconsource(self, id, size, wildcard = False):
		"Loads an icon as an iconsource"
		# FIXME: port
		return

		width, height	= Gtk.icon_size_lookup(size)
		pixbuf		= self.get_pixbuf(id, width)

		if pixbuf == None:
			return

		# reject icons more than 4 pixels away from requested size if not wildcard
		elif wildcard == False and not width - 4 <= pixbuf.get_property("width") <= width + 4:
			return

		elif wildcard == False and not height - 4 <= pixbuf.get_property("height") <= height + 4:
			return

		source = Gtk.IconSource()
		source.set_pixbuf(pixbuf)
		source.set_size(size)
		source.set_size_wildcarded(wildcard)

		return source


	def get_pixbuf(self, id, size):
		"Loads an icon as a pixbuf"

		if self.theme.has_icon(id) == False:
			return None

		try:
			return self.theme.load_icon(id, size, 0)

		except GObject.GError:
			return None



##### ACTION HANDLING #####

class Action(Gtk.Action):
	"UI Manager Action"

	def __init__(self, name, label = None, tooltip = None, stock = "", important = False):
		Gtk.Action.__init__(self, name, label, tooltip, stock)

		if important == True:
			self.set_property("is-important", True)



class ActionGroup(Gtk.ActionGroup):
	"UI Manager Actiongroup"

	def add_action(self, action, accel = None):
		"Adds an action to the actiongroup"

		if accel == None:
			Gtk.ActionGroup.add_action(self, action)

		else:
			self.add_action_with_accel(action, accel)



class ToggleAction(Gtk.ToggleAction):
	"A toggle action item"

	def __init__(self, name, label, tooltip = None, stock = None):
		Gtk.ToggleAction.__init__(self, name, label, tooltip, stock)



class UIManager(Gtk.UIManager):
	"UI item manager"

	def __init__(self):
		GObject.GObject.__init__(self)

		self.connect("connect-proxy", self.__cb_connect_proxy)


	def __cb_connect_proxy(self, uimanager, action, widget):
		"Callback for connecting proxies to an action"

		if type(widget) in ( Gtk.MenuItem, Gtk.ImageMenuItem, Gtk.CheckMenuItem ):
			widget.tooltip = action.get_property("tooltip")

		else:
			widget.set_property("label", widget.get_property("label").replace("...", ""))


	def add_ui_from_file(self, file):
		"Loads ui from a file"

		try:
			Gtk.UIManager.add_ui_from_file(self, file)

		except GObject.GError:
			raise IOError


	def append_action_group(self, actiongroup):
		"Appends an action group"

		Gtk.UIManager.insert_action_group(self, actiongroup, len(self.get_action_groups()))


	def get_action(self, name):
		"Looks up an action in the managers actiongroups"

		for actiongroup in self.get_action_groups():
			action = actiongroup.get_action(name)

			if action is not None:
				return action


	def get_action_group(self, name):
		"Returns the named action group"

		for actiongroup in self.get_action_groups():
			if actiongroup.get_name() == name:
				return actiongroup



##### APPLICATION COMPONENTS #####

class App(Gtk.Window):
	"An application window"

	def __init__(self, appname):
		GObject.GObject.__init__(self)
		self.set_title(appname)

		self.toolbars = {}

		self.main_vbox = Gtk.VBox()

		self.statusbar = Statusbar()
		self.main_vbox.pack_end(self.statusbar, False, True, 0)

		self.add(self.main_vbox)

		self.uimanager = UIManager()
		self.add_accel_group(self.uimanager.get_accel_group())


	def __connect_menu_statusbar(self, menu):
		"Connects a menus items to the statusbar"

		for item in menu.get_children():
			if isinstance(item, Gtk.MenuItem) == True:
				item.connect("select", self.cb_menudesc, True)
				item.connect("deselect", self.cb_menudesc, False)


	def cb_menudesc(self, item, show):
		"Displays menu descriptions in the statusbar"

		if show == True:
			self.statusbar.set_status(item.tooltip)

		else:
			self.statusbar.clear()


	def __cb_toolbar_hide(self, widget, name):
		"Hides the toolbar dock when the toolbar is hidden"

		if name in self.toolbars:
			self.toolbars[name].hide()


	def __cb_toolbar_show(self, widget, name):
		"Shows the toolbar dock when the toolbar is shown"

		if name in self.toolbars:
			self.toolbars[name].show()


	def add_toolbar(self, toolbar, name, band, detachable):
		"Adds a toolbar"

		# TODO: This is not working correctly yet.
		if detachable:
			handlebox = Gtk.HandleBox()
			handlebox.add(toolbar)
			toolbar = handlebox

		self.toolbars[name] = toolbar
		self.main_vbox.pack_start(toolbar, False, True, 0)

		toolbar.connect("show", self.__cb_toolbar_show, name)
		toolbar.connect("hide", self.__cb_toolbar_hide, name)

		toolbar.show_all()


	def get_title(self):
		"Returns the app title"

		title = Gtk.Window.get_title(self)

		return title.replace(" - " + config.APPNAME, "")


	def popup(self, menu, button, time):
		"Displays a popup menu"

		self.__connect_menu_statusbar(menu)
		menu.popup(None, None, None, None, button, time)


	def run(self):
		"Runs the application"

		self.show_all()
		Gtk.main()


	def set_menus(self, menubar):
		"Sets the menubar for the application"

		for item in menubar.get_children():
			self.__connect_menu_statusbar(item.get_submenu())

		self.main_vbox.pack_start(menubar, False, True, 0)


	def set_title(self, title):
		"Sets the window title"

		Gtk.Window.set_title(self, title + " - " + config.APPNAME)


	def set_toolbar(self, toolbar):
		"Sets the application toolbar"

		self.main_vbox.pack_start(toolbar, False, True, 0)
		toolbar.connect("show", self.__cb_toolbar_show, "Toolbar")
		toolbar.connect("hide", self.__cb_toolbar_hide, "Toolbar")

	def set_contents(self, widget):
		self.main_vbox.pack_start(widget, True, True, 0)



class EntryView(VBox):
	"A component for displaying an entry"

	def __init__(self, cfg = None, clipboard = None):
		VBox.__init__(self)
		self.set_spacing(12)
		self.set_border_width(12)

		self.config		= cfg
		self.clipboard		= clipboard
		self.entry		= None


	def clear(self, force = False):
		"Clears the data view"

		self.entry = None

		for child in self.get_children():
			child.destroy()


	def display_entry(self, e):
		"Displays info about an entry"

		self.clear()
		self.entry = e

		if self.entry == None:
			return

		# set up metadata display
		metabox = VBox()
		self.pack_start(metabox)

		label = ImageLabel(
			"<span size=\"large\" weight=\"bold\">%s</span>" % util.escape_markup(e.name),
			e.icon, ICON_SIZE_DATAVIEW
		)
		# metabox.pack_start(Alignment(label, 0.5, 0.5, 0, 0))

		label = Label("<span weight=\"bold\">%s</span>%s" % ( e.typename + (e.description != "" and ": " or ""), util.escape_markup(e.description) ), Gtk.Justification.CENTER)
		metabox.pack_start(label, True, True, 0)

		# set up field list
		fields = [ field for field in e.fields if field.value != "" ]

		if len(fields) > 0:
			table = Table(2, len(fields))
			self.pack_start(table)

			for rowindex, field in zip(range(len(fields)), fields):
				label = Label("<span weight=\"bold\">%s:</span>" % util.escape_markup(field.name))
				table.attach(label, 0, rowindex)

				widget = generate_field_display_widget(field, self.config, self.clipboard)
				table.attach(widget, 1, rowindex)

		# notes
		label = Label("<span weight=\"bold\">%s</span>%s" % ((e.notes != "" and _("Notes: ") or ""),
			util.escape_markup(e.notes) ), Gtk.Justification.LEFT)
		self.pack_start(label)

		# display updatetime
		if type(e) != entry.FolderEntry:
			label = Label((_('Updated %s ago') + "\n%s") % ( util.time_period_rough(e.updated, time.time()), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(e.updated)) ), Gtk.Justification.CENTER)
			self.pack_start(label)

		self.show_all()


	def pack_start(self, widget):
		"Adds a widget to the data view"

		alignment = Alignment(widget, 0.5, 0.5, 0, 0)
		VBox.pack_start(self, alignment, False, False, 0)



class Searchbar(Toolbar):
	"A toolbar for easy searching"

	def __init__(self):
		Toolbar.__init__(self)

		self.label		= Label("  " + _('  Find:') + " ")
		self.entry		= Entry()
		self.dropdown		= EntryDropDown()
		self.dropdown.insert_item(0, _('Any type'), "gnome-stock-about")
		self.button_next	= Button(STOCK_NEXT)
		self.button_prev	= Button(STOCK_PREVIOUS)

		self.append_widget(self.label)
		self.append_widget(self.entry, _('Text to search for'))
		self.append_widget(EventBox(self.dropdown), _('The type of account to search for'))
		self.append_space()
		self.append_widget(self.button_next, _('Find the next match'))
		self.append_widget(self.button_prev, _('Find the previous match'))

		self.connect("show", self.__cb_show)

		self.entry.connect("changed", self.__cb_entry_changed)
		self.entry.connect("key-press-event", self.__cb_key_press)

		self.button_next.set_sensitive(False)
		self.button_prev.set_sensitive(False)


	def __cb_entry_changed(self, widget, data = None):
		"Callback for entry changes"

		s = self.entry.get_text() != ""

		self.button_next.set_sensitive(s)
		self.button_prev.set_sensitive(s)


	def __cb_key_press(self, widget, data = None):
		"Callback for key presses"

		# return
		if data.keyval == 65293 and widget.get_text() != "":
			if data.state & Gdk.ModifierType.SHIFT_MASK == Gdk.ModifierType.SHIFT_MASK:
				self.button_prev.activate()

			else:
				self.button_next.activate()

			return True


	def __cb_show(self, widget, data = None):
		"Callback for widget display"

		self.entry.select_region(0, -1)
		self.entry.grab_focus()

