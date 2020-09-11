class Coinage:
    def __init__(self, cp, sp=0, ep=0, gp=0, pp=0):
        self.cp = cp
        self.sp = sp
        self.ep = ep
        self.gp = gp
        self.pp = pp

    def _downconvert(self):
        conv_gp = self.pp * 10
    
        conv_ep = (conv_gp + self.gp) * 2

        conv_sp = (conv_ep + self.ep) * 5
        
        conv_cp = (conv_sp + self.sp) * 10
        
        end_cp = conv_cp + self.cp

        return end_cp

    def convert(self, all="n"):
        conv_sp = self.cp // 10
        end_cp = self.cp % 10

        conv_ep = (self.sp + conv_sp) // 5
        end_sp = (self.sp + conv_sp) % 5

        conv_gp = (self.ep + conv_ep) // 2
        end_ep = (self.ep + conv_ep) % 2
        
        if all == "y":
            conv_pp = (self.gp + conv_gp) // 10
            end_gp = (self.gp + conv_gp) % 10

            end_pp = self.pp + conv_pp
        
        else:
            end_gp = self.gp + conv_gp

            end_pp = self.pp

        return f"You now have {end_cp} copper, {end_sp} silver, {end_ep} electrum, {end_gp} gold, and {end_pp} platinum."
        
    def calc_party(self):
        conv_sp = self.cp // 10
        end_cp = self.cp % 10

        conv_ep = (self.sp + conv_sp) // 5
        end_sp = (self.sp + conv_sp) % 5

        conv_gp = (self.ep + conv_ep) // 2
        end_ep = (self.ep + conv_ep) % 2

        end_gp = self.gp + conv_gp

        end_pp = self.pp

        return f"Everyone can add {end_cp} copper, {end_sp} silver, {end_ep} electrum, {end_gp} gold, and {end_pp} platinum to their character sheets."


