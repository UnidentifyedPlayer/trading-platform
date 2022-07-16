# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contractor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id = models.BigIntegerField(unique=True)
    part_of_object_id = models.BigIntegerField(blank=True, null=True)
    state_id = models.BigIntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    start_id = models.BigIntegerField(blank=True, null=True)
    start_req_id = models.BigIntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    end_id = models.BigIntegerField(blank=True, null=True)
    end_req_id = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_appl_user_id = models.BigIntegerField(blank=True, null=True)
    create_appl_user_lbl = models.CharField(max_length=200, blank=True, null=True)
    create_sys_user = models.CharField(max_length=40, blank=True, null=True)
    create_user_host = models.CharField(max_length=40, blank=True, null=True)
    create_user_ip_addr = models.CharField(max_length=40, blank=True, null=True)
    create_os_user = models.CharField(max_length=40, blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    last_update_appl_user_id = models.BigIntegerField(blank=True, null=True)
    last_update_appl_user_lbl = models.CharField(max_length=200, blank=True, null=True)
    last_update_sys_user = models.CharField(max_length=40, blank=True, null=True)
    last_update_user_host = models.CharField(max_length=40, blank=True, null=True)
    last_update_user_ip_addr = models.CharField(max_length=40, blank=True, null=True)
    last_update_os_user = models.CharField(max_length=40, blank=True, null=True)
    lbl = models.CharField(max_length=4000, blank=True, null=True)
    head_doc = models.CharField(max_length=4000, blank=True, null=True)
    country_old = models.CharField(max_length=4000, blank=True, null=True)
    license = models.CharField(max_length=4000, blank=True, null=True)
    name_full = models.CharField(max_length=4000, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    telephone = models.CharField(max_length=4000, blank=True, null=True)
    fax = models.CharField(max_length=4000, blank=True, null=True)
    list_work = models.CharField(max_length=4000, blank=True, null=True)
    name_short = models.CharField(max_length=4000, blank=True, null=True)
    region = models.CharField(max_length=4000, blank=True, null=True)
    reg_no = models.CharField(max_length=4000, blank=True, null=True)
    address = models.CharField(max_length=4000, blank=True, null=True)
    email_address = models.CharField(max_length=4000, blank=True, null=True)
    info = models.CharField(max_length=4000, blank=True, null=True)
    oe_start_date = models.DateTimeField(blank=True, null=True)
    reg_author = models.CharField(max_length=4000, blank=True, null=True)
    address_urd = models.CharField(max_length=4000, blank=True, null=True)
    www = models.CharField(max_length=4000, blank=True, null=True)
    inn = models.CharField(max_length=4000, blank=True, null=True)
    manufacturer = models.BigIntegerField(blank=True, null=True)
    kpp = models.CharField(max_length=4000, blank=True, null=True)
    okpo = models.CharField(max_length=4000, blank=True, null=True)
    okato = models.CharField(max_length=4000, blank=True, null=True)
    imnc = models.CharField(max_length=4000, blank=True, null=True)
    ogrn = models.CharField(max_length=4000, blank=True, null=True)
    bankers = models.CharField(max_length=4000, blank=True, null=True)
    last_name = models.CharField(max_length=4000, blank=True, null=True)
    first_name = models.CharField(max_length=4000, blank=True, null=True)
    mid_name = models.CharField(max_length=4000, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    birth_place = models.CharField(max_length=4000, blank=True, null=True)
    fd_001 = models.BinaryField(blank=True, null=True)
    ft_001 = models.CharField(max_length=200, blank=True, null=True)
    fn_001 = models.CharField(max_length=200, blank=True, null=True)
    passport_no = models.CharField(max_length=4000, blank=True, null=True)
    passport_author = models.CharField(max_length=4000, blank=True, null=True)
    passport_date = models.DateTimeField(blank=True, null=True)
    mpng_mdm_id = models.CharField(max_length=4000, blank=True, null=True)
    role_flag_customer = models.BigIntegerField(blank=True, null=True)
    role_flag_supplier = models.BigIntegerField(blank=True, null=True)
    b_accreditation = models.BigIntegerField(blank=True, null=True)
    role_flag_operator = models.BigIntegerField(blank=True, null=True)
    opf_old = models.BigIntegerField(blank=True, null=True)
    norbit_buid = models.CharField(max_length=4000, blank=True, null=True)
    fd_charter = models.BinaryField(blank=True, null=True)
    ft_charter = models.CharField(max_length=200, blank=True, null=True)
    fn_charter = models.CharField(max_length=200, blank=True, null=True)
    fd_registr_certificate = models.BinaryField(blank=True, null=True)
    ft_registr_certificate = models.CharField(max_length=200, blank=True, null=True)
    fn_registr_certificate = models.CharField(max_length=200, blank=True, null=True)
    fd_registr_tax_authority = models.BinaryField(blank=True, null=True)
    ft_registr_tax_authority = models.CharField(max_length=200, blank=True, null=True)
    fn_registr_tax_authority = models.CharField(max_length=200, blank=True, null=True)
    fd_appointment_order = models.BinaryField(blank=True, null=True)
    ft_appointment_order = models.CharField(max_length=200, blank=True, null=True)
    fn_appointment_order = models.CharField(max_length=200, blank=True, null=True)
    fd_egryul = models.BinaryField(blank=True, null=True)
    ft_egryul = models.CharField(max_length=200, blank=True, null=True)
    fn_egryul = models.CharField(max_length=200, blank=True, null=True)
    fd_excel_price = models.BinaryField(blank=True, null=True)
    ft_excel_price = models.CharField(max_length=200, blank=True, null=True)
    fn_excel_price = models.CharField(max_length=200, blank=True, null=True)
    accreditation_date = models.DateTimeField(blank=True, null=True)
    egrpo_cert = models.BinaryField(blank=True, null=True)
    ft_egrpo_cert = models.CharField(max_length=200, blank=True, null=True)
    fn_egrpo_cert = models.CharField(max_length=200, blank=True, null=True)
    okud_1 = models.BinaryField(blank=True, null=True)
    ft_okud_1 = models.CharField(max_length=200, blank=True, null=True)
    fn_okud_1 = models.CharField(max_length=200, blank=True, null=True)
    producer_status_cert = models.BinaryField(blank=True, null=True)
    ft_producer_status_cert = models.CharField(max_length=200, blank=True, null=True)
    fn_producer_status_cert = models.CharField(max_length=200, blank=True, null=True)
    customers_references = models.BinaryField(blank=True, null=True)
    ft_customers_references = models.CharField(max_length=200, blank=True, null=True)
    fn_customers_references = models.CharField(max_length=200, blank=True, null=True)
    uldoc_changes_cert = models.BinaryField(blank=True, null=True)
    ft_uldoc_changes_cert = models.CharField(max_length=200, blank=True, null=True)
    fn_uldoc_changes_cert = models.CharField(max_length=200, blank=True, null=True)
    accr_order = models.BinaryField(blank=True, null=True)
    ft_accr_order = models.CharField(max_length=200, blank=True, null=True)
    fn_accr_order = models.CharField(max_length=200, blank=True, null=True)
    egryul_cert = models.BinaryField(blank=True, null=True)
    ft_egryul_cert = models.CharField(max_length=200, blank=True, null=True)
    fn_egryul_cert = models.CharField(max_length=200, blank=True, null=True)
    scntr = models.BinaryField(blank=True, null=True)
    ft_scntr = models.CharField(max_length=200, blank=True, null=True)
    fn_scntr = models.CharField(max_length=200, blank=True, null=True)
    scntr_date = models.DateTimeField(blank=True, null=True)
    scntr_num = models.BigIntegerField(blank=True, null=True)
    scntr_type = models.BigIntegerField(blank=True, null=True)
    pref_lang = models.BigIntegerField(blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, db_column='country')
    opf = models.CharField(max_length=4000, blank=True, null=True)
    oos_username = models.CharField(max_length=4000, blank=True, null=True)
    oos_password = models.CharField(max_length=4000, blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_rnp = models.BigIntegerField(blank=True, null=True)
    small_business = models.BigIntegerField(blank=True, null=True)
    type_id = models.BigIntegerField(blank=True, null=True)
    role_flag_seller_mrk = models.BigIntegerField(blank=True, null=True)
    role_flag_customer_mrk = models.BigIntegerField(blank=True, null=True)
    consent_check = models.BigIntegerField(blank=True, null=True)
    consent_date = models.DateTimeField(blank=True, null=True)
    fd_inn_cert = models.BinaryField(blank=True, null=True)
    ft_inn_cert = models.CharField(max_length=200, blank=True, null=True)
    fn_inn_cert = models.CharField(max_length=200, blank=True, null=True)
    fd_consent_upd = models.BinaryField(blank=True, null=True)
    ft_consent_upd = models.CharField(max_length=200, blank=True, null=True)
    fn_consent_upd = models.CharField(max_length=200, blank=True, null=True)
    fl_charter = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_contractor'


class Country(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id = models.BigIntegerField(unique=True)
    part_of_object_id = models.BigIntegerField(blank=True, null=True)
    state_id = models.BigIntegerField()
    start_date = models.DateTimeField(blank=True, null=True)
    start_id = models.BigIntegerField(blank=True, null=True)
    start_req_id = models.BigIntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    end_id = models.BigIntegerField(blank=True, null=True)
    end_req_id = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    create_date = models.DateTimeField()
    create_appl_user_id = models.BigIntegerField(blank=True, null=True)
    create_appl_user_lbl = models.CharField(max_length=200, blank=True, null=True)
    create_sys_user = models.CharField(max_length=40, blank=True, null=True)
    create_user_host = models.CharField(max_length=40, blank=True, null=True)
    create_user_ip_addr = models.CharField(max_length=40, blank=True, null=True)
    create_os_user = models.CharField(max_length=40, blank=True, null=True)
    last_update_date = models.DateTimeField()
    last_update_appl_user_id = models.BigIntegerField(blank=True, null=True)
    last_update_appl_user_lbl = models.CharField(max_length=200, blank=True, null=True)
    last_update_sys_user = models.CharField(max_length=40, blank=True, null=True)
    last_update_user_host = models.CharField(max_length=40, blank=True, null=True)
    last_update_user_ip_addr = models.CharField(max_length=40, blank=True, null=True)
    last_update_os_user = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_country'
