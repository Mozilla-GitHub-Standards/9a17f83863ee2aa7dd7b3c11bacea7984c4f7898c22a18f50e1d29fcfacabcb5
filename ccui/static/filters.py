# Case Conductor is a Test Case Management system.
# Copyright (C) 2011 uTest Inc.
# 
# This file is part of Case Conductor.
# 
# Case Conductor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Case Conductor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Case Conductor.  If not, see <http://www.gnu.org/licenses/>.
from ..core.filters import FieldFilter



class TestCycleStatusFilter(FieldFilter):
    options = [
        (1, "draft"),
        (2, "active"),
        (3, "locked"),
        ]



class TestRunStatusFilter(FieldFilter):
    options = [
        (1, "draft"),
        (2, "active"),
        (3, "locked"),
        ]



class TestSuiteStatusFilter(FieldFilter):
    options = [
        (1, "draft"),
        (2, "active"),
        (3, "locked"),
        ]



class TestCaseStatusFilter(FieldFilter):
    options = [
        (1, "draft"),
        (2, "active"),
        (3, "locked"),
        ]



class ApprovalStatusFilter(FieldFilter):
    options = [
        (1, "pending"),
        (2, "approved"),
        (3, "rejected"),
        ]



class TestResultStatusFilter(FieldFilter):
    options = [
        (1, "pending"),
        (2, "passed"),
        (3, "failed"),
        (5, "started"),
        (6, "invalid"),
        ]
