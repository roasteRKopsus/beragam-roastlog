
from django.contrib import admin

from .models import *
from import_export.admin import ExportActionMixin
from daterangefilter.filters import PastDateRangeFilter
from django_admin_listfilter_dropdown.filters import ( DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter)
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce
from import_export import resources
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from django.contrib.admin.views.main import ChangeList
from django.db.models import Count, Sum
from datetime import date
from production.admin import RoastedMaterialInline

today = datetime.date.today()
time_delta = timedelta(hours=12)
today+=time_delta



# class ClientNameResource(resources.ModelResource):


# 	code = fields.Field(attribute='code')
# 	beans_name = fields.Field(attribute='beans_name')
# 	jenis_kopi = fields.Field(attribute='jenis_kopi')
# 	variety = fields.Field(attribute='variety')
# 	origin = fields.Field(attribute='origin')
# 	paska_panen = fields.Field(attribute='paska_panen')
# 	vendor_name = fields.Field(attribute='vendor_name')
# 	stock_terupdate = fields.Field(attribute='stock_terupdate')
# 	nilai_stock = fields.Field(attribute='nilai_stock')


class ForeignMaterialItemInline(admin.StackedInline):


	model = ForeignMaterialItem
	extra=0


class BeansCodeResource(resources.ModelResource):


	code = fields.Field(attribute='code')
	beans_name = fields.Field(attribute='beans_name')
	jenis_kopi = fields.Field(attribute='jenis_kopi')
	variety = fields.Field(attribute='variety')
	origin = fields.Field(attribute='origin')
	paska_panen = fields.Field(attribute='paska_panen')
	vendor_name = fields.Field(attribute='vendor_name')
	stock_terupdate = fields.Field(attribute='stock_terupdate')
	nilai_stock = fields.Field(attribute='nilai_stock')


class RoasterResource(resources.ModelResource):


	roast_date = fields.Field(attribute='roast_date')
	beans_name = fields.Field(
		attribute='beans_name',
		column_name='beans_name',
		widget=ForeignKeyWidget(BeansGudang, 'beans_name')
		)
	BlendName_name = fields.Field(
		attribute='blend_name',
		column_name='blend_name',
		widget=ForeignKeyWidget(BlendName, 'blend_name')
		)
	mesin = fields.Field(attribute='mesin')
	shift = fields.Field(attribute='shift')
	process = fields.Field(attribute='process')
	batch_number= fields.Field(attribute='batch_number')
	beans_color = fields.Field(attribute='beans_color')
	density = fields.Field(attribute='density')
	moisture = fields.Field(attribute='moisture_content')
	raw = fields.Field(attribute='raw')
	roasted = fields.Field(attribute='roasted')
	persentase_susut = fields.Field(attribute='persentase_susut')
	auto_check = fields.Field(attribute='auto_control_weight')
	weight_params = fields.Field(attribute='weight_parameters')
	roaster_pass_check = fields.Field(attribute='roaster_pass_check')
	roaster_name = fields.Field(attribute='roaster_shift_name')
	catatan_roaster = fields.Field(attribute='catatan_roaster')	
	umur_roastbean = fields.Field(attribute='umur_roastbean')



class PengambilanGreenbeanResource(resources.ModelResource):


	beans_name = fields.Field(
        column_name='beans_name',
        attribute='beans_name',
        widget=ForeignKeyWidget(BeansGudang, 'beans_name'))

	class Meta:
		model = PengambilanGreenbean


class BeansGudangResource(resources.ModelResource):


	last_update = fields.Field(attribute='last_update')
	sample_code = fields.Field(
		attribute='sample_code',
		column_name='beans_name',
		widget=ForeignKeyWidget(BeansCode, 'sample_code')
		)
	beans_name = fields.Field(attribute='beans_name')
	jenis_kopi = fields.Field(attribute='jenis_kopi')
	variety = fields.Field(attribute='variety')
	origin =  fields.Field(attribute='origin')
	paska_panen = fields.Field(attribute='paska_panen') 
	crop_year = fields.Field(attribute='Crop_year')
	vendor_name = fields.Field(attribute='vendor_name')
	lot_number  = fields.Field(attribute='lot_number')
	bag =  fields.Field(attribute='bag')
	qty_bag = fields.Field(attribute='qty_bag')
	inherited_stock = fields.Field(attribute='inherited_stock')
	initial_stock = fields.Field(attribute='initial_stock')
	price_kilo_idr = fields.Field(attribute='price_kilo_idr')
	stock_status = fields.Field(attribute='stock_status')
	stock_update = fields.Field(attribute='stock_akhir')
	beans_usage_amount = fields.Field(attribute='beans_usage_amount')
	beans_usage_value = fields.Field(attribute='beans_usage_value')
	beans_usage_percent = fields.Field(attribute='beans_usage_percent')
	depreciation_average = fields.Field(attribute='depreciation_average')
	roasted = fields.Field(attribute='roasted')
	qc_acceptance = fields.Field(attribute='qc_acceptance')
	moisture_check = fields.Field(attribute='moisture_check')
	primary_defect = fields.Field(attribute='primary_defect')
	secondary_defect = fields.Field(attribute='secondary_defect')
	aroma_greenbean = fields.Field(attribute='aroma_greenbean')
	fragrance_score = fields.Field(attribute='fragrance_score')
	fragrance_intensity = fields.Field(attribute='fragrance_intensity')
	fragrance_notes = fields.Field(attribute='fragrance_notes')
	flavor_score = fields.Field(attribute='flavor_score')
	flavor_intensity = fields.Field(attribute='flavor_intensity')
	flavor_notes = fields.Field(attribute='flavor_notes')
	aftertaste_score = fields.Field(attribute='aftertaste_score')
	aftertaste_notes = fields.Field(attribute='aftertaste_notes')
	acidity_score = fields.Field(attribute='acidity_score')
	acidity_intensity = fields.Field(attribute='acidity_intensity')
	acidity_notes = fields.Field(attribute='acidity_notes')
	body_score = fields.Field(attribute='body_score')
	body_intensity = fields.Field(attribute='body_intensity')
	body_notes = fields.Field(attribute='body_notes')
	balance_score = fields.Field(attribute='balance_score')
	uniformity_score = fields.Field(attribute='uniformity_score')
	cleancup_score = fields.Field(attribute='cleancup_score')
	overal_cup = fields.Field(attribute='overal_cup')
	defect = fields.Field(attribute='defect')
	cup_score = fields.Field(attribute='cup_score')


class BeansCodeAdmin(ExportActionMixin, admin.ModelAdmin):


	list_display= (


	'code',
	'client_name',
	'beans_name',
	'jenis_kopi',
	'variety',
	'origin',
	'paska_panen',
	'vendor_name',
	'stock_terupdate',
	'nilai_stock'

		)

	list_filter= (


	'code',
	'beans_name',
	'jenis_kopi',
	'variety',
	'origin',
	'paska_panen',
	'vendor_name'

	)

	list_editable= ['client_name']

	resource_class = BeansCodeResource


class ClientNameAdmin(ExportActionMixin, admin.ModelAdmin):
	list_display = (
		'client_code',
		'client_name',
		'pic',
		'no_telp',
		'alamat'
		)

	list_filter = (
		'client_code',
		'client_name',
		'pic',
		)



class BeansGudangAdmin(ExportActionMixin, admin.ModelAdmin):


	list_display = (
		'sample_code',
		'show_this',
		'beans_name',
		'owner',
		'cup_score',
		'stock_status',
		'vendor_name',
		'lot_number',
		'qc_check',
		'bag',
		'inherited_stock','UOM',
		'initial_stock','UOM',
		'stock_akhir','UOM',
		'beans_usage_amount',
		'beans_usage_percent',
		'beans_usage_value',
		
		'roasted',
		'depreciation_average',


		'last_update',
		
		
		)

	list_filter=(
		('lot_number',PastDateRangeFilter),
		'beans_name',
		'sample_code',
		# 'stock_status',
		'vendor_name',
		('lot_number',PastDateRangeFilter),
		'qc_check',
		
		
		)

	list_editable = ['show_this',]


	resource_class = BeansGudangResource


class PengambilanGreenbeanAdmin(ExportActionMixin, admin.ModelAdmin):


	list_display =(
	'tanggal',
	'beans_name',
	'blend_name',
	'jumlah_diambil',
	'UOM',
	'GB_value',
	'mesin',
	'shifts',
	'pic',
	'keterangan',
	
)
	list_filter =(
	
	('tanggal',PastDateRangeFilter),
	('beans_name', RelatedDropdownFilter),
	('blend_name', RelatedDropdownFilter),
	'jumlah_diambil',
	'mesin',
	'shifts',
	'pic',
	'keterangan'
)

	resource_class = PengambilanGreenbeanResource
	

class RoasterAdmin(ExportActionMixin, admin.ModelAdmin):



	list_display = ('roast_date',
	'beans_name',
	'blend_name',
	'mesin',
	'shift',
	'roaster',
	'batch_number',
	'set_number',
	'roastcode',
	'moisture_content',
	'raw',
	'UOM',
	'roasted',
	'UOM',
	'persentase_susut',
	'roaster_pass_check',
	'weight_parameters',
	'machine_weight_loss',
	'catatan_roaster',
	'umur_roastbean',
	'next_process',
	'ganti_status',
	)


	list_editable =['next_process', 'blend_name']
	list_max_show_all = 100
	list_per_page = 20

	exclude = ['next_process']

	list_filter=(('roast_date', PastDateRangeFilter),'mesin','shift','roaster_pass_check', ('beans_name', RelatedDropdownFilter),('blend_name', RelatedDropdownFilter))
	# prepopulated_fields = {'susut':('persentase_susut')}

	list_max_show_all = 1000

	resource_class = RoasterResource


	def changelist_view(self, request, extra_context=None):

		roasted_daily = []
		qs = Roaster.objects.all()
		froco15 = qs.filter(roast_date = today).filter(mesin= 'froco-15').aggregate(Sum('roasted'))
		froco25 = qs.filter(roast_date = today).filter(mesin= 'froco-25').aggregate(Sum('roasted'))

		context = {
		'froco15' : froco15,
		'froco25' : froco25,
		
		}
		return super().changelist_view(request, extra_context=context)

		inlines = [
			RoastedMaterialInline
		]


class BlendNameAdmin(ExportActionMixin, admin.ModelAdmin):


	list_display = ('blend_name','show_this', 
		'daily_blend', 'week_1','week_2','week_3',
		'week_4','week_5','latest','deficiency','monthly_target')
	list_filter = ('blend_name', 'periode' )

	list_editable = ['show_this', 'monthly_target']


class RoasterNameAdmin(ExportActionMixin, admin.ModelAdmin):


	list_display = ('roaster_technician',
		'created_date', 
		'telp',
		'address'
		)




class RoastErrorLogsAdmin(ExportActionMixin, admin.ModelAdmin):



	list_display = ('date_time', 
		'roastcode',
		'machine',
		'kronology',
		'resolution')
	list_filter = (('date_time', PastDateRangeFilter), 'machine')

class ForeignMaterialReportAdmin(ExportActionMixin, admin.ModelAdmin):
	list_display = ('created_date','shift', 'reporter')
	list_filter = (('created_date',PastDateRangeFilter), 'reporter')
	inlines = [ForeignMaterialItemInline]


class ForeignMaterialItemAdmin(ExportActionMixin,admin.ModelAdmin):
	list_display = ('created', 'nama_item', 'berat')


admin.site.register(BeansCode, BeansCodeAdmin)
admin.site.register(BeansGudang, BeansGudangAdmin)
admin.site.register(Roaster, RoasterAdmin)
admin.site.register(PengambilanGreenbean, PengambilanGreenbeanAdmin)
admin.site.register(BlendName, BlendNameAdmin)
admin.site.register(RoasterName, RoasterNameAdmin)
admin.site.register(RoastErrorLogs, RoastErrorLogsAdmin)
admin.site.register(ClientName, ClientNameAdmin)
admin.site.register(ForeignMaterialReport, ForeignMaterialReportAdmin)
admin.site.register(ForeignMaterialItem, ForeignMaterialItemAdmin)
# admin.site.register(ForeignMaterialItem, ForeignMaterialItemAdmin)



