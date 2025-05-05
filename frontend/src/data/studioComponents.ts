import { createListResource } from "frappe-ui"

const studioComponents = createListResource({
	method: "GET",
	doctype: "Studio Component",
	fields: ["name", "component_name", "studio_app", "creation", "modified"],
	auto: true,
	cache: "customComponents",
	orderBy: "creation asc",
	pageLength: 50,
})

export { studioComponents }
