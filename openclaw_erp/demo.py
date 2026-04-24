from __future__ import annotations

import json


def build_nig_commerce_context():
	monthly = [
		{"month": "Jan", "actual": 2.1, "forecast": 2.0},
		{"month": "Feb", "actual": 2.3, "forecast": 2.2},
		{"month": "Mar", "actual": 2.5, "forecast": 2.4},
		{"month": "Apr", "actual": 2.6, "forecast": 2.5},
		{"month": "May", "actual": 2.8, "forecast": 2.7},
		{"month": "Jun", "actual": 3.0, "forecast": 2.9},
		{"month": "Jul", "actual": 3.2, "forecast": 3.1},
		{"month": "Aug", "actual": 3.1, "forecast": 3.0},
		{"month": "Sep", "actual": 2.9, "forecast": 3.0},
		{"month": "Oct", "actual": 2.7, "forecast": 2.8},
		{"month": "Nov", "actual": 3.4, "forecast": 3.2},
		{"month": "Dec", "actual": 4.1, "forecast": 3.8},
	]

	margin_matrix = [
		{"sku": "NIG-ULTRA-01", "dtc": 44, "marketplace": 31, "retail": 28, "wholesale": 22},
		{"sku": "NIG-HOME-07", "dtc": 37, "marketplace": 26, "retail": 25, "wholesale": 18},
		{"sku": "NIG-LUX-12", "dtc": 52, "marketplace": 35, "retail": 30, "wholesale": 24},
		{"sku": "NIG-CORE-03", "dtc": 33, "marketplace": 24, "retail": 20, "wholesale": 16},
	]

	return {
		"title": "Nig Commerce Command Center",
		"kpis": [
			{"label": "Gross Merchandise Value", "value": "$48.6M", "delta": "+18.4%", "tone": "up"},
			{"label": "Net Revenue", "value": "$32.1M", "delta": "+12.8%", "tone": "up"},
			{"label": "Contribution Margin", "value": "27.3%", "delta": "+2.1 pts", "tone": "up"},
			{"label": "Perfect Order Rate", "value": "96.8%", "delta": "+1.7 pts", "tone": "up"},
		],
		"channels": [
			{"name": "DTC Web", "revenue": "$12.8M", "share": "39%", "conversion": "4.7%", "service": "99.1%"},
			{"name": "Marketplace", "revenue": "$9.3M", "share": "29%", "conversion": "3.9%", "service": "97.4%"},
			{"name": "Retail B2B", "revenue": "$6.2M", "share": "19%", "conversion": "2.8%", "service": "98.7%"},
			{"name": "Wholesale", "revenue": "$3.8M", "share": "13%", "conversion": "2.1%", "service": "96.2%"},
		],
		"pipeline": [
			{"stage": "Order Capture", "count": 1842, "sla": "99.8%", "status": "stable"},
			{"stage": "Payment Review", "count": 138, "sla": "93.2%", "status": "watch"},
			{"stage": "Picking", "count": 426, "sla": "97.6%", "status": "stable"},
			{"stage": "Packing", "count": 271, "sla": "95.1%", "status": "watch"},
			{"stage": "Dispatch", "count": 702, "sla": "98.3%", "status": "stable"},
			{"stage": "Returns Processing", "count": 89, "sla": "88.9%", "status": "risk"},
		],
		"alerts": [
			{
				"severity": "Critical",
				"title": "Marketplace return spike on premium accessories",
				"detail": "Returns reached 8.4% this week, 2.3x above baseline. Margin risk estimated at $182K.",
			},
			{
				"severity": "High",
				"title": "North Hub replenishment breach in 11 days",
				"detail": "Eight A-class SKUs will fall below service stock if inbound ETA slips by more than 48 hours.",
			},
			{
				"severity": "Medium",
				"title": "VIP account renewal at risk",
				"detail": "Three enterprise buyers show declining basket frequency and slower collections behavior.",
			},
		],
		"customers": [
			{"name": "Harbor Retail Group", "segment": "Enterprise B2B", "ltv": "$4.8M", "margin": "31%", "risk": "Low"},
			{"name": "Metro Style Holdings", "segment": "Marketplace Partner", "ltv": "$3.9M", "margin": "22%", "risk": "Medium"},
			{"name": "Northline Flagship", "segment": "DTC VIP", "ltv": "$2.4M", "margin": "43%", "risk": "Low"},
			{"name": "Atlas Department Stores", "segment": "Wholesale", "ltv": "$5.2M", "margin": "18%", "risk": "High"},
		],
		"warehouses": [
			{"name": "London DC", "utilization": 82, "accuracy": "99.4%", "fill_rate": "98.7%"},
			{"name": "Midlands Hub", "utilization": 74, "accuracy": "98.9%", "fill_rate": "97.9%"},
			{"name": "North Hub", "utilization": 91, "accuracy": "97.6%", "fill_rate": "94.8%"},
		],
		"timeline": [
			{"time": "08:15", "event": "Board trading pack refreshed", "owner": "Finance Control Tower"},
			{"time": "08:42", "event": "Demand forecast uplifted for home tech bundle", "owner": "Planning AI"},
			{"time": "09:20", "event": "Returns anomaly escalated to category lead", "owner": "CX Ops"},
			{"time": "10:05", "event": "Enterprise renewal risk flagged for Atlas", "owner": "Revenue Ops"},
			{"time": "11:10", "event": "Emergency replenishment PO drafted", "owner": "Procurement Desk"},
		],
		"dataset_json": json.dumps({"monthly": monthly, "margin_matrix": margin_matrix}),
	}
