CATEGORIES = ['laptop', 'tablet', 'monitor', 'eBook', 'fridge', 'freezer', 'electric_stoves', 'multicooker', 'meet_grinder', 'microwave']
SHOPS = ['sulpak', 'technodom', 'mechta', 'veter' ]
SHOP_CLASSES = ['Sulpak', 'Technodom', 'Mechta', 'Veter']

DOMAINS = {
	"sulpak": "https://www.sulpak.kz/f/",
	"technodom": "https://www.technodom.kz/",
	"mechta": "https://www.mechta.kz/api/main/catalog_new/index.php?catalog=true&page_num={}&page_element_count=100000&section=",
	"veter": "https://shop.kz/"
}

PAGES_NAMES = {
	"sulpak": {
		"laptop": "noutbuki",
		"tablet": "planshetiy",
		"monitor": "monitoriy",
		"eBook": "elektronniye_knigi",
	},
	"technodom": {
	},
	"mechta": {
		"laptop": "noutbuki",
		"tablet": "planshety",
		"monitor": "monitory",
		"eBook": "elektronnye-knigi",
		"fridge": "holodilniki",
		"freezer": "morozilniki",
		"electric_stoves": "elektricheskie-plity",
		"multicooker": "multivarki",
		"meet_grinder": "myasorubki",
		"microwave": "mikrovolnovye-pechi",
	},
	"veter": {
		"laptop": "noutbuki/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/",
		"tablet": "planshety/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/",
		"monitor": "monitory/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/",
		"eBook": "elektronnye-knigi/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/",
		"fridge": "kholodilniki/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/",
		"freezer": "morozilniki/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/",
		"electric_stoves": "plity/filter/fltr_type_control-is-elektricheskaya/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/",
		"multicooker": "multivarki-parovarki/filter/almaty-is-v_nalichii-or-dostavim/fltr_device_type-is-multivarka/apply/",
		"meet_grinder": "elektromyasorubki/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/",
		"microwave": "mikrovolnovki/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/",
	},
}
