from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

#获取当前包的安装地址
packagepath = get_package_share_directory('arm1')
print(packagepath)

#读取urdf文件
urdfpath=packagepath+'/urdf/robot_ros2_control.urdf'
robot_desc=open(urdfpath).read()

def generate_launch_description():
    
    robot_desc_node=Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[
            {'robot_description': robot_desc},
        ]
    )

    cm_node= Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[packagepath+'/config/robot_ros2_controllers.yaml'],
        output="both",
    )

    cn_node=Node(package="controller_manager",
        executable="spawner",
        arguments=['position_controller', 'joint_state_broadcaster'],
        output="screen",
    )

    rviz_node=Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        arguments=[ '-d', packagepath+'/urdf/arm_rviz.rviz', ],
    )
    jc_node=Node(
        package='arm1',
        executable='joint_control',
    )

    return LaunchDescription([
        robot_desc_node,
        cm_node,
        cn_node,
        rviz_node,
        jc_node
    ])
