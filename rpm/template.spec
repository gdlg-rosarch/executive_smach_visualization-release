Name:           ros-lunar-smach-viewer
Version:        2.0.2
Release:        0%{?dist}
Summary:        ROS smach_viewer package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/smach_viewer
Source0:        %{name}-%{version}.tar.gz

Requires:       graphviz
Requires:       ros-lunar-smach-msgs
Requires:       ros-lunar-smach-ros
Requires:       wxPython-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-rostest

%description
The smach viewer is a GUI that shows the state of hierarchical SMACH state
machines. It can visualize the possible transitions between states, as well as
the currently active state and the values of user data that is passed around
between states. The smach viewer uses the SMACH debugging interface based on the
smach messages to gather information from running state machines.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Oct 26 2017 Jonathan Bohren <jbo@jhu.edu> - 2.0.2-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Jonathan Bohren <jbo@jhu.edu> - 2.0.1-0
- Autogenerated by Bloom

