from django.utils import timezone
from dateutil.relativedelta import relativedelta

from edc_constants.constants import (POS, YES, NO, NOT_APPLICABLE)
from edc_sync.models import OutgoingTransaction

from td_maternal.models import MaternalVisit

from .base_test_case import BaseTestCase
from .factories import (MaternalEligibilityFactory, MaternalConsentFactory, AntenatalEnrollmentFactory)


class TestOutgoingTransactions(BaseTestCase):

    def setUp(self):
        pass

    def test_outgoing_transactions_created(self):
        super(TestOutgoingTransactions, self).setUp()
        maternal_eligibility = MaternalEligibilityFactory()
        self.assertNotEqual(OutgoingTransaction.objects.all().count(), 0)
        self.assertTrue(OutgoingTransaction.objects.filter(tx_name='td_maternal.maternaleligibility').exists())
        self.options = {'registered_subject': maternal_eligibility.registered_subject,
                        'current_hiv_status': POS,
                        'evidence_hiv_status': YES,
                        'will_get_arvs': YES,
                        'is_diabetic': NO,
                        'will_remain_onstudy': YES,
                        'rapid_test_done': NOT_APPLICABLE,
                        'last_period_date': (timezone.datetime.now() - relativedelta(weeks=25)).date()}
        MaternalConsentFactory(registered_subject=maternal_eligibility.registered_subject)
        self.assertTrue(OutgoingTransaction.objects.filter(tx_name='td_maternal.maternalconsent').exists())
        AntenatalEnrollmentFactory(**self.options)
        self.assertTrue(OutgoingTransaction.objects.filter(tx_name='td_maternal.antenatalenrollment').exists())
        self.assertTrue(MaternalVisit.objects.all().exists())
        self.assertTrue(OutgoingTransaction.objects.filter(tx_name='td_maternal.maternalvisit').exists())

