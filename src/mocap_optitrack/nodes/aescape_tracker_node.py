#!/usr/bin/env python3

import rospy
import tf

from aescape_python.util.tf_helper import TFHelper
from mocap_optitrack.util.constants import (
    OPTITRACK_TRACKER_FREQUENCY,
    OPTITRACK_TRACKER_NAMESPACE,
)
from mocap_optitrack.managers.calibration_manager import OptitrackCalibrationManager


class OptitrackTrackerNode:
    def __init__(self):
        rospy.init_node("optitrack_tracker_node")

        self.broadcaster = tf.TransformBroadcaster()
        self.rate = rospy.Rate(OPTITRACK_TRACKER_FREQUENCY)
        self._init()
        self.calibration_manager = OptitrackCalibrationManager()

    def _init(self):
        self.tf_helper = TFHelper()

    def run(self):
        rospy.loginfo("Started optitrack tracker node.")
        rospy.spin()


if __name__ == "__main__":
    optitrack_tracker_node = OptitrackTrackerNode()

    try:
        optitrack_tracker_node.run()
    except rospy.ROSInterruptException:
        pass
