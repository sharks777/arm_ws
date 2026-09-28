from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

# 获取当前包arm1的安装地址
packagepath = get_package_share_directory('arm1')
print(packagepath)

# 读取urdf文件
urdfpath = packagepath + '/urdf/robot.urdf'
robot_desc = open(urdfpath).read()

def generate_launch_description():
    # 节点1：robot_state_publisher，发布机器人模型和tf坐标
    robot_desc_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[
            {'robot_description': robot_desc},
        ]
    )

    # 节点2：joint_state_publisher_gui，关节滑块控制面板
    joint_state_pub_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
    )

    # 节点3：rviz2可视化，自动加载保存好的rviz配置文件
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        arguments=['-d', packagepath+'/urdf/rviz.rviz'],
    )

    # 返回所有要启动的节点
    return LaunchDescription([
        robot_desc_node,
        joint_state_pub_node,
        rviz_node,
    ])
