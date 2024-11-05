from enum import Enum


class MatchState(Enum):
    IN_PROGRESS = 1
    DELAYED = 2
    HALTED = 3
    COMPLETED = 4
    UPCOMING = 5


class InningsState(Enum):
    UPCOMING = 1
    IN_PROGRESS = 2
    COMPLETED = 3


class InningsOrder(Enum):
    FIRST = 1
    SECOND = 2
    UNDECIDED = 3


class BallResult(Enum):
    DOT = 0
    SINGLE = 1
    DOUBLE = 2
    TRIPLE = 3
    FOUR = 4
    SIX = 6
    WIDE = 7
    NO_BALL = 8
    WICKET = 9


class PlayerRole(Enum):
    BATSMAN = 1
    BOWLER = 2
    ALL_ROUNDER = 3
