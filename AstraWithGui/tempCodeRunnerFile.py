
        super(MainThread, self).__init__()

    def run(self):
        global returnaction

        pythoncom.CoInitialize()
        
        self.speakfunc("Say wakeup to continue !!")
        returnaction("Sleeping...")
        while True: