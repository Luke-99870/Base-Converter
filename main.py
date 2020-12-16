import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window 
from kivy.uix.screenmanager import  *
from kivy.properties import StringProperty
import numpy as np
Builder.load_file("kivydesign.kv")
Config.set('kivy','window_icon','noun_Clone Trooper_207435.ico')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand') #Disable stupid red dots
Window.size = (1000,700) 

#########################
class MenuScr(Screen):    
    pass
#########################
class CalcScrUnsigBin(Screen):
    def UnsignedBinaryInputs(self, button):
        prior = self.ids.UnsigBinInput.text
        if prior == "Enter your Unsigned Binary Number":
            self.ids.UnsigBinInput.text = button
        else:
            self.ids.UnsigBinInput.text = f'{button}{prior}'

    def SubmitUnsignedBinary(self):
        self.ids.UnsignedBinaryDenary.text = "Denary: "
        self.ids.UnsignedBinaryHexadecimal.text = "Hexadecimal: "

        BinaryInput = self.ids.UnsigBinInput.text
        BinaryDenaryConversion = self.ids.UnsignedBinaryDenary.text
        BinaryHexaConversion = self.ids.UnsignedBinaryHexadecimal.text

        self.ids.UnsignedBinaryDenary.text = f'{BinaryDenaryConversion}{str(int(BinaryInput, 2))}'
        UnsignedBinaryHexConversion = str(hex(int(BinaryInput, 2)))
        UnsignedBinaryHexConversionReplaced = UnsignedBinaryHexConversion.replace("0x","")
        self.ids.UnsignedBinaryHexadecimal.text = f'{BinaryHexaConversion}{UnsignedBinaryHexConversionReplaced.upper()}'
        self.ids.UnsigBinInput.text = "Enter your Unsigned Binary Number"

class CalcScrDen (Screen):
    def DenaryInputsNegative(self, button):
        prior = self.ids.DenaryInput.text
        if prior == "Enter your Denary Number":
            pass
        elif "-" in prior:
             self.ids.DenaryInput.text = prior.replace("-","")
        else:
            self.ids.DenaryInput.text = f'-{prior}'
    def DenaryInputs(self, button):
        prior = self.ids.DenaryInput.text
        if prior == "Enter your Denary Number":
            self.ids.DenaryInput.text = button
        else:
            self.ids.DenaryInput.text = f'{prior}{button}'

    def RemoveADigit(self):
        prior = self.ids.DenaryInput.text
        if prior != "Enter your Denary Number":   
            prior = prior[:-1]
            self.ids.DenaryInput.text = prior
        else:
            pass

    def DenarySubmit(self):
        self.ids.DenaryUnsignedBinary.text = "Unsigned Binary: "
        self.ids.DenarySignMagnitude.text = "Sign & Magnitude: "
        self.ids.DenaryTwoComplement.text = "Two's Complement: "
        self.ids.DenaryHexadecimal.text = "Hexadecimal: "

        DenaryInput = self.ids.DenaryInput.text
        if "-" in DenaryInput:
            self.ids.DenaryUnsignedBinary.font_size = 0
            self.ids.DenarySignMagnitude.pos_hint = {"top": 1.04, "x": 0.15}
            self.ids.DenaryTwoComplement.pos_hint = {"top": 0.95, "x": 0.15}
            self.ids.DenaryHexadecimal.font_size = 0
            SignMagNegative = f'{np.binary_repr(int(DenaryInput.replace("-","")),8)}'
            self.ids.DenarySignMagnitude.text = f'{self.ids.DenarySignMagnitude.text}1{SignMagNegative}'
            
            self.ids.DenaryTwoComplement.text = f'{self.ids.DenaryTwoComplement.text}{np.binary_repr(int(DenaryInput),8)}'

        else:
            self.ids.DenaryUnsignedBinary.font_size = 20
            self.ids.DenarySignMagnitude.pos_hint = {"top": 1.1, "x": 0.15}
            self.ids.DenaryTwoComplement.pos_hint = {"top": 0.9, "x": 0.15}
            self.ids.DenaryHexadecimal.font_size = 20
            self.ids.DenarySignMagnitude.text = f'{self.ids.DenarySignMagnitude.text}{np.binary_repr(int(DenaryInput),8)}'
            self.ids.DenaryTwoComplement.text = f'{self.ids.DenaryTwoComplement.text}{np.binary_repr(int(DenaryInput),8)}'
            DenaryHexadecimalConversion = str(hex(int(DenaryInput, 10)))
            DenaryHexadecimalReplaced = DenaryHexadecimalConversion.replace("0x","")
            self.ids.DenaryHexadecimal.text = f'{self.ids.DenaryHexadecimal.text}{DenaryHexadecimalReplaced.upper()}'

        
        self.ids.DenaryUnsignedBinary.text = f'{self.ids.DenaryUnsignedBinary.text}{np.binary_repr(int(DenaryInput),8)}'

        self.ids.DenaryInput.text = "Enter your Denary Number"
#########################

ScreenManagement = ScreenManager(transition=CardTransition())
ScreenManagement.add_widget(MenuScr(name='MenuScreen'))
ScreenManagement.add_widget(CalcScrUnsigBin(name='CalculationScreenUnsignedBinary'))
#ScreenManagement.add_widget(CalcScrUnsigBin(name='CalculationScreenUnsignedBinary'))
#ScreenManagement.add_widget(CalcScrUnsigBin(name='CalculationScreenUnsignedBinary'))
ScreenManagement.add_widget(CalcScrDen(name='CalculationScreenDenary'))
#ScreenManagement.add_widget(CalcScrUnsigBin(name='CalculationScreenUnsignedBinary'))

#########################

class BaseConverter(App): #Class set as BaseConverter app - it taking App from above
    def build(self): #Creates a function within self (App)
        Window.clearcolor = (82/255, 72/255, 156/255,1)
        return ScreenManagement

BaseConverter().run()