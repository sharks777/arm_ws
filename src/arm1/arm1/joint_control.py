import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray


class MultiArrayPublisher(Node):
    def __init__(self):
        super().__init__('multiarray_publisher')
        self.publisher_ = self.create_publisher(
            Float64MultiArray,
            'position_controller/commands',
            10
        )
        timer_period = 1.0  # 发布频率1Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = Float64MultiArray()
        msg.data = [self.counter / 10.0]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg}"')
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = MultiArrayPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
