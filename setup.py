import os
import distutils.core

distutils.core.setup(
    name='testenv',
    version=os.environ['TESTENV_VERSION'],
    description=(
        'Deploy and tear down environments of several virtual machines'
    ),
    license='GNU GPLv2+',
    author='Dima Kuznetsov',
    author_email='dkuznets@redhat.com',
    url='redhat.com',
    package_dir={
        'testenv': 'lib/testenv',
        'ovirttestenv': 'contrib/ovirt/lib/ovirttestenv'
    },
    packages=['testenv', 'ovirttestenv'],
    package_data={
        'testenv': [
            '*.xml',
            '*.log.conf',
        ],
    },
    provides=['testenv', 'ovirttestenv'],
    scripts=[
        'testenv/testenvcli',
        'contrib/ovirt/ovirttestenv/testenvcli-ovirt',
    ],
    data_files=[
        (
            'share/testenv',
            [
                'bin/sync_templates.py',
                'bin/update_images.py',
            ],
        ),
        (
            'share/testenv/setup_scripts',
            [
                'scripts/update_if_needed.sh',
            ],
        ),
        (
            'share/ovirttestenv/config/repos',
            [
                'contrib/ovirt/config/repos/ovirt-3.5-external.repo',
                ('contrib/ovirt/config/repos/'
                    'ovirt-master-snapshot-external.repo'),
                'contrib/ovirt/config/repos/ovirt-master-snapshot.repo',
            ],
        ),
        (
            'share/ovirttestenv/config/virt',
            [
                'contrib/ovirt/config/virt/centos6.json',
                'contrib/ovirt/config/virt/centos7.json',
                'contrib/ovirt/config/virt/rhel7.json',
            ],
        ),
        (
            'share/ovirttestenv/config/deploy',
            [
                'contrib/ovirt/config/deploy/scripts.json',
            ],
        ),
        (
            'share/ovirttestenv/config/answer-files',
            [
                'contrib/ovirt/config/answer-files/el6_master.conf',
                'contrib/ovirt/config/answer-files/el7_master.conf',
                'contrib/ovirt/config/answer-files/el6_3.5.conf',
                'contrib/ovirt/config/answer-files/el7_3.5.conf',
            ],
        ),
        (
            'share/ovirttestenv/setup_scripts',
            [
                'contrib/ovirt/setup_scripts/add_local_repo.sh',
                'contrib/ovirt/setup_scripts/setup_engine.sh',
                'contrib/ovirt/setup_scripts/setup_host.sh',
                'contrib/ovirt/setup_scripts/setup_storage_iscsi.sh',
                'contrib/ovirt/setup_scripts/setup_storage_nfs.sh',
            ],
        ),
        (
            'share/ovirttestenv/test_scenarios',
            [
                'contrib/ovirt/test_scenarios/bootstrap.py',
                'contrib/ovirt/test_scenarios/create_clean_snapshot.py',
                'contrib/ovirt/test_scenarios/basic_sanity.py',
            ],
        ),
        (
            'libexec/ovirttestenv',
            [
                'contrib/ovirt/libexec/build_engine_rpms.sh',
                'contrib/ovirt/libexec/build_vdsm_rpms.sh',
            ],
        ),
        (
            '/etc/testenv.d/',
            [
                'etc/testenv.d/testenv.conf',
                'contrib/ovirt/etc/testenv.d/ovirt.conf',
            ],
        ),
        (
            '/etc/mock',
            [
                'contrib/ovirt/mock/epel-6-x86_64_ovirt.cfg',
                'contrib/ovirt/mock/epel-7-x86_64_ovirt.cfg',
            ],
        ),
        (
            '/etc/firewalld/services',
            [
                'contrib/ovirt/firewalld/services/testenv.xml',
            ],
        ),
        (
            '/etc/polkit-1/localauthority/50-local.d/',
            [
                'polkit/testenv.pkla',
            ],
        ),
        (
            '/etc/sudoers.d',
            [
                'sudo/testenv',
            ],
        ),
        (
            '/var/lib/testenv/subnets',
            [],
        ),
        (
            '/var/lib/testenv/store',
            [],
        ),
        (
            '/var/lib/testenv/reposync',
            [],
        ),
    ],
)
