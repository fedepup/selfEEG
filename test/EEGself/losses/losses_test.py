import unittest
import os
import sys
import itertools
import numpy as np
import torch

sys.path.append(os.getcwd().split('/test')[0])
from selfeeg import losses



class TestLoss(unittest.TestCase):

    def makeGrid(self, pars_dict):  
        keys=pars_dict.keys()
        combinations=itertools.product(*pars_dict.values())
        ds=[dict(zip(keys,cc)) for cc in combinations]
        return ds

    @classmethod
    def setUpClass(cls):
        cls.device= torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
        if cls.device.type == 'cpu':
            cls.device  = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        device = cls.device
        print('\n---------------------')
        print('TESTING LOSSES MODULE')
        if cls.device.type != 'cpu':
            print('Found other device: testing nn.modules with both cpu and gpu')
        else:
            print('Didn\'t found cuda device: testing nn.modules with only cpu')
        print('---------------------')
        N, Feat = 64, 128
        cls.N       = 64
        cls.Feat    = 128
        cls.x  = torch.randn(N,Feat)
        cls.y  = torch.randn(N,Feat)
        cls.p  = torch.randn(N,Feat)
        cls.z  = torch.randn(N,Feat)
        cls.u  = torch.randn(Feat, 1024)
        
        if device.type != 'cpu':
            cls.x2  = torch.randn(N,Feat).to(device=device)
            cls.y2  = torch.randn(N,Feat).to(device=device)
            cls.p2  = torch.randn(N,Feat).to(device=device)
            cls.z2  = torch.randn(N,Feat).to(device=device)
            cls.u2  = torch.randn(Feat, 1024).to(device=device)

    def setUp(self):
        self.seed=1234
        np.random.seed(self.seed)
        torch.manual_seed(self.seed)

    
    def test_barlowLoss(self):
        print('Testing Barlow Loss...', end="", flush=True)
        Barlow_args = {'z1': [self.x],'z2': [self.y,None], 'lambda_coeff': [0.005, 0.05, 0.5, 1]}
        Barlow_args = self.makeGrid(Barlow_args)
        for i in Barlow_args:
            loss = losses.Barlow_loss(**i)
            self.assertTrue(torch.isnan(loss).sum()==0)

        if self.device.type != 'cpu':
            Barlow_args = {'z1': [self.x2],'z2': [self.y2,None], 
                           'lambda_coeff': [0.005, 0.05, 0.5, 1]}
            Barlow_args = self.makeGrid(Barlow_args)
            for i in Barlow_args:
                loss = losses.Barlow_loss(**i)
                self.assertTrue(torch.isnan(loss).sum()==0)
        
        x  = torch.sin(torch.linspace(0,8*torch.pi,self.Feat) ) + (torch.arange(self.N)/self.N).unsqueeze(1)
        loss = losses.Barlow_loss(x)
        self.assertTrue( (loss-76.4043)<1e-4)
        print('   Barlow Loss OK: tested', len(Barlow_args), 'combinations of input arguments')

    
    
    def test_BYOLLoss(self):
        print('Testing BYOL Loss...', end="", flush=True)
        BYOL_args = {'z1': [self.x],'z2': [self.y],'p1': [self.p],'p2': [self.z], 
                     'projections_norm': [True,False]}
        BYOL_args = self.makeGrid(BYOL_args)
        for i in BYOL_args:
            loss = losses.BYOL_loss(**i)
            self.assertTrue(torch.isnan(loss).sum()==0)
        
        if self.device.type != 'cpu':
            BYOL_args = {'z1': [self.x2],'z2': [self.y2],'p1': [self.p2],'p2': [self.z2], 
                         'projections_norm': [True,False]}
            BYOL_args = self.makeGrid(BYOL_args)
            for i in BYOL_args:
                loss = losses.BYOL_loss(**i)
                self.assertTrue(torch.isnan(loss).sum()==0)

        x= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/6) + (torch.arange(self.N)/self.N).unsqueeze(1)
        y= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/4 ) + (torch.arange(self.N)/self.N).unsqueeze(1)
        p= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/3) + (torch.arange(self.N)/self.N).unsqueeze(1)
        z= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/5) + (torch.arange(self.N)/self.N).unsqueeze(1)
        loss = losses.BYOL_loss(x,y,p,z)
        self.assertTrue( (loss-0.0534)<1e-4)
        print('   BYOL Loss OK: tested', len(BYOL_args), 'combinations of input arguments')

    

    def test_SimCLRLoss(self):
        print('Testing SimCLR Loss...', end="", flush=True)
        SimCLR_args = {'projections': [self.x],'temperature':[0.15, 0.5, 0.7], 
                       'projections_norm': [True,False]}
        SimCLR_args = self.makeGrid(SimCLR_args)
        for i in SimCLR_args:
            loss = losses.SimCLR_loss(**i)
            self.assertTrue(torch.isnan(loss).sum()==0)
        
        if self.device.type != 'cpu':
            SimCLR_args = {'projections': [self.x],'temperature':[0.15, 0.5, 0.7], 
                           'projections_norm': [True,False]}
            SimCLR_args = self.makeGrid(SimCLR_args)
            for i in SimCLR_args:
                loss = losses.SimCLR_loss(**i)
                self.assertTrue(torch.isnan(loss).sum()==0)

        x = torch.sin(torch.linspace(0,8*torch.pi,self.Feat) + torch.pi/6)+ (torch.arange(self.N)/self.N).unsqueeze(1)
        loss = losses.SimCLR_loss(x)
        self.assertTrue( (loss-9.04887)<1e-4)
        print('   SimCLR Loss OK: tested', len(SimCLR_args), 'combinations of input arguments')

    

    def test_SimSiamLoss(self):
        print('Testing SimSiam Loss...', end="", flush=True)
        Siam_args = {'z1': [self.x],'z2': [self.y],'p1': [self.p],'p2': [self.z], 
                     'projections_norm': [True,False]}
        Siam_args = self.makeGrid(Siam_args)
        for i in Siam_args:
            loss = losses.SimSiam_loss(**i)
            self.assertTrue(torch.isnan(loss).sum()==0)
        
        if self.device.type != 'cpu':
            Siam_args = {'z1': [self.x2],'z2': [self.y2],'p1': [self.p2],'p2': [self.z2], 
                         'projections_norm': [True,False]}
            Siam_args = self.makeGrid(Siam_args)
            for i in Siam_args:
                loss = losses.SimSiam_loss(**i)
                self.assertTrue(torch.isnan(loss).sum()==0)
        x= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/6) + (torch.arange(self.N)/self.N).unsqueeze(1)
        y= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/4 ) + (torch.arange(self.N)/self.N).unsqueeze(1)
        p= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/3) + (torch.arange(self.N)/self.N).unsqueeze(1)
        z= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/5) + (torch.arange(self.N)/self.N).unsqueeze(1)
        loss = losses.SimSiam_loss(x,y,p,z)
        self.assertTrue( (loss-(-0.9867))<1e-4)
        print('   SimSiam Loss OK: tested', len(Siam_args), 'combinations of input arguments')


    def test_VICRegLoss(self):
        print('Testing VICReg Loss...', end="", flush=True)
        Vicreg_args = {'z1': [self.x],'z2': [self.y,None], 'Lambda': [25,10,50],
                       'Mu': [25,5,50], 'Nu': [2,1,0.5]}
        Vicreg_args = self.makeGrid(Vicreg_args)
        for i in Vicreg_args:
            loss = losses.VICReg_loss(**i)
            self.assertTrue(torch.isnan(loss).sum()==0)
        
        if self.device.type != 'cpu':
            Vicreg_args = {'z1': [self.x2],'z2': [self.y2,None], 
                           'Lambda': [25,10,50],'Mu': [25,5,50], 'Nu': [2,1,0.5]}
            Vicreg_args = self.makeGrid(Vicreg_args)
            for i in Vicreg_args:
                loss = losses.VICReg_loss(**i)
                self.assertTrue(torch.isnan(loss).sum()==0)
        
        x = torch.sin(torch.linspace(0,8*torch.pi,self.Feat) )+ (torch.arange(self.N)/self.N).unsqueeze(1)
        loss = losses.VICReg_loss(x)
        self.assertTrue( (loss-21.4443)<1e-4)
        print('   VICReg Loss OK: tested', len(Vicreg_args), 'combinations of input arguments')



    def test_MoCoLoss(self):
        print('Testing MoCo Loss...', end="", flush=True)
        Moco_args = {'q': [self.x],'k': [self.y], 'queue': [None, self.u],
                     'projections_norm': [True, False], 'temperature': [0.15, 0.5, 0.9]}
        Moco_args = self.makeGrid(Moco_args)
        for i in Moco_args:
            loss = losses.Moco_loss(**i)
            self.assertTrue(torch.isnan(loss).sum()==0)
        
        if self.device.type != 'cpu':
            Moco_args = {'q': [self.x],'k': [self.y], 'queue': [None, self.u],
                         'projections_norm': [True, False], 'temperature': [0.15, 0.5, 0.9]}
            Moco_args = self.makeGrid(Moco_args)
            for i in Moco_args:
                loss = losses.Moco_loss(**i)
                self.assertTrue(torch.isnan(loss).sum()==0)

        x= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/6) + (torch.arange(self.N)/self.N).unsqueeze(1)
        y= torch.sin(torch.linspace(0,8*torch.pi,self.Feat) +torch.pi/4 ) + (torch.arange(self.N)/self.N).unsqueeze(1)
        u= torch.sin(torch.linspace(0,8*torch.pi,1024) +torch.pi/3) + (torch.arange(self.Feat)/self.Feat).unsqueeze(1)
        loss = losses.Moco_loss(x,y,u)
        self.assertTrue( (loss-108.6667)<1e-4)
        loss = losses.Moco_loss(x,y)
        self.assertTrue( (loss-0.4952)<1e-4)
        print('   MoCo Loss OK: tested', len(Moco_args), 'combinations of input arguments')

