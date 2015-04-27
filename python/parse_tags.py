#!/usr/bin/env python
import os

tags = """
    10
    10g
    14.04
    admin
    agent
    astute
    backports-4.1.1
    bare-metal
    baremetal
    bnx2x
    bonding
    bootstrap
    bvt
    cciss
    ceilometer
    ceph
    ci
    ci-status
    ci-testing
    cinder
    cli
    cobbler
    cold-restart-improvements
    conductor
    content-lenght-range
    contrail
    controller
    corosync
    customer-found
    db
    deadlocks
    devops
    dhcp
    dns
    dnsmasq
    docker
    docs
    ephemeral
    eth
    ethx
    experimental
    fakeui
    feature
    feature-advanced-networking
    feature-bonding
    feature-deadlocks
    feature-demo-site
    feature-hardware-change
    feature-image-based
    feature-logging
    feature-mongo
    feature-multi-l2
    feature-native-provisioning
    feature-plugins
    feature-progress-bar
    feature-redeployment
    feature-remote-repos
    feature-reset-env
    feature-security
    feature-simple-mode
    feature-stats
    feature-stop-deployment
    feature-tasks
    feature-upgrade
    feature-validation
    firewall
    fpb
    fuel
    fuel-astute
    fuel-ci
    fuel-cli
    fuel-devops
    fuel-docs
    fuel-library
    fuel-main
    fuel-plugins
    fuel-registration
    fuel-web
    fuelmenu
    fuelupgrade
    galera
    gerrit
    gig
    glance
    granular
    gro
    gso
    ha
    ha-guide
    haproxy
    havana-backport-potential
    heat
    horizon
    hwrequest
    icehouse
    icehouse-backport-potential
    image-based
    in
    in-stable-icehouse
    infrastructure
    inprogress
    iptables
    iso
    jenkins
    json
    juno
    keystone
    known-issues
    l23
    l23network
    library
    license
    locale
    log
    logging
    logs
    low-hanging-fruit
    make
    master-slave
    mcagent
    mellanox
    migration
    mirror
    mirrors
    ml2
    module-build
    module-client
    module-fuelmenu
    module-master-node-installation
    module-nailgun
    module-nailgun-agent
    module-netcheck
    module-networks
    module-ostf
    module-serialization
    module-shotgun
    module-tasks
    module-volumes
    mongo
    mongodb
    monitoring
    mos
    mos-linux
    multi-l3
    multiple-cluster-networks
    murano
    mysql
    nailgun
    nailgun-agent
    netprobe
    networking
    neutron
    new-repo
    newcomers-docs
    nic
    nova
    nova.conf
    nsx
    offload
    on-verification
    openstack
    operations
    ops
    osci
    osci-package
    osft
    ostf
    ostf-adapter
    ovs
    pacemaker
    package
    packages
    parnter
    partial-content
    partner
    patch-openstack
    patching
    performance
    pi-board
    plugin
    plugins
    progress
    provision
    pumphouse
    puppet
    pxe
    python
    python-fuelclient
    qa
    qemu
    rabbit
    rabbitmq
    rados
    radosgw
    raid
    release-notes
    release-notese
    report-exporter
    review
    rpm
    ruby2
    s-size
    sahara
    scale
    sclae
    script
    security
    seed
    shotgun
    size-l
    size-m
    size-s
    sorting
    ssd
    staging
    statistics
    stats
    storage
    supervisor
    swift
    system-test-added
    system-test-not-required
    system-tests
    tech-debt
    techtalk
    testrail
    timeout
    to-be-covered-by-tests
    ubuntu
    ubuntu14
    ubuntu1404
    ui
    unified-objects
    unit-tests
    update
    upgrade
    vbox-scripts
    vcenter
    verification-done
    version
    virtualbox
    vmdk
    vmware
    volumes
    zabbix
""".split("\n    ")

people = """
    fuel-python
    fuel-astute
    fuel-provisioning
    fuel-build
    alekseyk-ru
    dshulyak
    rustyrobot
    ikalnitsky
    nmarkov
    aroma-x
    akislitsky
    kozhukalov
    dpyzhov
    a-gordeev
    ivankliuk
    vsharshov
    maciej-iai
    sbrzeczkowski
    ksambor
    prmtl
    pkaminski
    romcheg
    loles
""".split("\n    ")

teams = """
    fuel-python
    fuel-astute
    fuel-provisioning
    fuel-build
""".split("\n    ")

status_pre = "field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&"
ml_pre = "field.milestone%3Alist=68007&"
pre = status_pre + ml_pre

print "<h1>Tags</h1><table><tr><th>Tag"

for t in teams:
    team = t.strip()
    if team:
        print "<th>%s" % team

print "</tr>"

for t in tags:
    tag = t.strip()
    if tag and (tag.startswith("feature-") or tag.startswith("module-") or tag=="tech-debt" or tag=="customer-found"):
        print "<tr>"
        url = "https://bugs.launchpad.net/fuel/+bugs?%sfield.tag=%s" % (pre, tag)
        count = os.popen("curl '%s' 2> /dev/null | grep -B 1 -m 1 '            result' | head -n 1" % url).read()
        print "<td><a href='%s'>%s (%s)</a>" % (url, tag, count.strip())
        for team_r in teams:
            team = team_r.strip()
            if team:
                url = "https://bugs.launchpad.net/fuel/+bugs?%sfield.tag=%s&field.assignee=%s" % (pre, tag, team)
                count = os.popen("curl '%s' 2> /dev/null | grep -B 1 -m 1 '            result' | head -n 1" % url).read()
                print "<td><a href='%s'>%s</a>" % (url, count.strip())
        print "</tr>"

print "</table>"

print "<h1>People</h1>"

for p in people:
    person = p.strip()
    if person:
        url = "https://bugs.launchpad.net/~%s/+bugs?%sfield.assignee=%s" % (person, pre, person)
        count = os.popen("curl '%s' 2> /dev/null | grep -B 1 -m 1 '            result' | head -n 1" % url).read()
        print "<a href='%s'>%s (%s)</a>" % (url, person, count.strip())
