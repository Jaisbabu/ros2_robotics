import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloRobot(Node):
    def __init__(self):
        super().__init__('hello_robot')
        self.publisher_ = self.create_publisher(
            String, 'robot_messages', 10
        )
        self.timer = self.create_timer(1.0, self.publish_message)
        self.count = 0

    def publish_message(self):
        msg = String()
        msg.data = f'Hello from my robot! Message {self.count}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = HelloRobot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
