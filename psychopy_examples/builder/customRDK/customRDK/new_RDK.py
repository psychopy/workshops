#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from psychopy.visual.dot import DotStim

import numpy
from numpy import reshape


class NewRDK(DotStim):
    
    def _update_dotsXY(self):
        #  The function in psychopy/visual/dot is pasted below but 
        # here we've changed it to make ALL dots grow/shrink
        
        if self.dir>0:
            self._verticesBase = self._verticesBase*1.005
        else:
            self._verticesBase = self._verticesBase/1.005
            
        # update the pixel XY coordinates in pixels (using _BaseVisual class)
        self._updateVertices()
        
        
        
"""
    
    def _update_dotsXY(self):

        # Find dead dots, update positions, get new positions for
        # dead and out-of-bounds
        # renew dead dots
        if self.dotLife > 0:  # if less than zero ignore it
            # decrement. Then dots to be reborn will be negative
            self._dotsLife -= 1
            dead = (self._dotsLife <= 0.0)
            self._dotsLife[dead] = self.dotLife
        else:
            dead = numpy.zeros(self.nDots, dtype=bool)

        # update XY based on speed and dir
        # NB self._dotsDir is in radians, but self.dir is in degs
        # update which are the noise/signal dots
        if self.signalDots == 'different':
            #  **up to version 1.70.00 this was the other way around,
            # not in keeping with Scase et al**
            # noise and signal dots change identity constantly
            numpy.random.shuffle(self._dotsDir)
            # and then update _signalDots from that
            self._signalDots = (self._dotsDir == (self.dir * pi / 180))

        # update the locations of signal and noise; 0 radians=East!
        reshape = numpy.reshape
        if self.noiseDots == 'walk':
            # noise dots are ~self._signalDots
            sig = numpy.random.rand((~self._signalDots).sum())
            self._dotsDir[~self._signalDots] = sig * pi * 2
            # then update all positions from dir*speed
            cosDots = reshape(numpy.cos(self._dotsDir), (self.nDots,))
            sinDots = reshape(numpy.sin(self._dotsDir), (self.nDots,))
            self._verticesBase[:, 0] += self.speed * cosDots
            self._verticesBase[:, 1] += self.speed * sinDots
        elif self.noiseDots == 'direction':
            # simply use the stored directions to update position
            cosDots = reshape(numpy.cos(self._dotsDir), (self.nDots,))
            sinDots = reshape(numpy.sin(self._dotsDir), (self.nDots,))
            self._verticesBase[:, 0] += self.speed * cosDots
            self._verticesBase[:, 1] += self.speed * sinDots
        elif self.noiseDots == 'position':
            # update signal dots
            sd = self._signalDots
            sdSum = self._signalDots.sum()
            cosDots = reshape(numpy.cos(self._dotsDir[sd]), (sdSum,))
            sinDots = reshape(numpy.sin(self._dotsDir[sd]), (sdSum,))
            self._verticesBase[sd, 0] += self.speed * cosDots
            self._verticesBase[sd, 1] += self.speed * sinDots
            # update noise dots
            dead = dead + (~self._signalDots)  # just create new ones

        # handle boundaries of the field
        if self.fieldShape in (None, 'square', 'sqr'):
            dead0 = (numpy.abs(self._verticesBase[:, 0]) > 0.5)
            dead1 = (numpy.abs(self._verticesBase[:, 1]) > 0.5)
            dead = dead + dead0 + dead1

        elif self.fieldShape == 'circle':
            # transform to a normalised circle (radius = 1 all around)
            # then to polar coords to check
            # the normalised XY position (where radius should be < 1)
            normXY = self._verticesBase / 0.5
            # add out-of-bounds to those that need replacing
            dead = dead + (numpy.hypot(normXY[:, 0], normXY[:, 1]) > 1)

        # update any dead dots
        if sum(dead):
            self._verticesBase[dead, :] = self._newDotsXY(sum(dead))

        # update the pixel XY coordinates in pixels (using _BaseVisual class)
        self._updateVertices()
"""