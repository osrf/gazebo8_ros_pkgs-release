Name:           ros-hydro-gazebo-plugins
Version:        2.3.7
Release:        0%{?dist}
Summary:        ROS gazebo_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://gazebosim.org/wiki/Tutorials#ROS_Integration
Source0:        %{name}-%{version}.tar.gz

Requires:       gazebo-devel
Requires:       ros-hydro-angles
Requires:       ros-hydro-camera-info-manager
Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-driver-base
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-gazebo-msgs
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-message-generation
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-nodelet
Requires:       ros-hydro-pcl-conversions
Requires:       ros-hydro-polled-camera
Requires:       ros-hydro-rosconsole
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rosgraph-msgs
Requires:       ros-hydro-rospy
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-srvs
Requires:       ros-hydro-tf
Requires:       ros-hydro-tf2-ros
Requires:       ros-hydro-trajectory-msgs
Requires:       ros-hydro-urdf
BuildRequires:  gazebo-devel
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-camera-info-manager
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-diagnostic-updater
BuildRequires:  ros-hydro-driver-base
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-gazebo-msgs
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-nodelet
BuildRequires:  ros-hydro-pcl-conversions
BuildRequires:  ros-hydro-polled-camera
BuildRequires:  ros-hydro-rosconsole
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rosgraph-msgs
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-srvs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-tf2-ros
BuildRequires:  ros-hydro-trajectory-msgs
BuildRequires:  ros-hydro-urdf

%description
Robot-independent Gazebo plugins for sensors, motors and dynamic reconfigurable
components.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Sep 01 2014 John Hsu <hsu@osrfoundation.org> - 2.3.7-0
- Autogenerated by Bloom

* Mon Aug 18 2014 John Hsu <hsu@osrfoundation.org> - 2.3.6-0
- Autogenerated by Bloom

