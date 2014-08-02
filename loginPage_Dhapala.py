#-------------------------------------------------------------------------------
# Name:        LOGIN page
# Purpose:
#
# Author:      Ganesh
#
# Created:     27/07/2014
# Copyright:   (c) Sandhya 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx

########################################################################
class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, 1729,title="Login", pos=(300,300), size=(300,200))
        self.logged_in = False

        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, 1730,label="Username:")
        user_sizer.Add(user_lbl, 0, wx.ALL|wx.CENTER, 5)


        self.user = wx.TextCtrl(self, 1731)
        user_sizer.Add(self.user, 0, wx.ALL, 5)

        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, 1732,label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL|wx.CENTER, 5)

        self.password = wx.TextCtrl(self, 1733,style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogin)
        p_sizer.Add(self.password, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)

        # Button

        btn = wx.Button(self, label="Login")
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        #Login yes or no

        errorMsg = wx.StaticText(self, 1734, label="")
        errorMsg.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        main_sizer.Add(errorMsg, 0, wx.ALL, 5)

        self.SetSizer(main_sizer)

    #----------------------------------------------------------------------
    def onLogin(self, event):
        """
        Check credentials and login
        """
        stupid_username = "user"
        stupid_password = "pass"
        user_password = self.password.GetValue()
        user_name = self.user.GetValue()
        if user_password == stupid_password and user_name == stupid_username:
            print "You are now logged in!"
            self.logged_in = True
            self.Close()
        else:
            errorDlg = wx.MessageBox("Username or Password is wrong. Please try again", "Login Error")
            dlg = LoginDialog()
            dlg.GetChildren()
            print "Username or password is incorrect!"

########################################################################
class MyPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)


########################################################################
class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Main App")
        panel = MyPanel(self)

        # Ask user to login
        dlg = LoginDialog()
        dlg.ShowModal()
        authenticated = dlg.logged_in
        if not authenticated:
            self.Close()

        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

def main():
    pass
