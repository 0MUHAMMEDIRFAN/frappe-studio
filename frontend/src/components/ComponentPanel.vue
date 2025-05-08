<template>
	<div class="flex flex-col gap-5">

		<!-- Component Filter -->
		<div class="sticky top-[41px] z-50 mt-[-15px] flex w-full bg-white py-3">
			<TextInput type="text" size="sm" class="w-full" variant="outline" placeholder="Search component" v-model="componentFilter" @input="(e: Event) => (componentFilter = (e.target as HTMLInputElement).value)" />
		</div>

		<!-- Custom Components -->
		<div class="grid grid-cols-2 items-center gap-x-2 gap-y-4">
			<div v-for="component in store.appComponents" :key="component.name">
				<div class="flex cursor-grab flex-col items-center justify-center gap-2 text-gray-700" draggable="true" @dragstart="(ev) => canvasStore.handleDragStart(ev, component.name)" @dragend="(_ev) => canvasStore.handleDragEnd()">
					<div class="w-full group flex items-center justify-center gap-2 truncate rounded border-[1px] border-gray-300 bg-gray-50 p-4 transition duration-300 ease-in-out">
						<!-- <LucideIcon name="settings" class="h-6 w-6" /> -->
						<span class="w-full truncate text-xs">{{ component.component_name || component.name }}</span>

						<!-- Menu -->
						<div class="ml-auto flex items-center gap-1.5 text-gray-600 group-hover:visible has-[.active-item]:visible">
							<Dropdown :options="getComponentMenu()" trigger="click">
								<template v-slot="{ open }">
									<button class="flex cursor-pointer items-center rounded-sm p-0.5 text-gray-700 hover:bg-gray-300" :class="open ? 'active-item' : ''">
										<FeatherIcon name="more-horizontal" class="h-4 w-4" />
									</button>
								</template>
							</Dropdown>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Real Components -->
		<div class="grid grid-cols-3 items-center gap-x-2 gap-y-4">
			<div v-for="component in componentList" :key="component.name">
				<div class="flex cursor-grab flex-col items-center justify-center gap-2 text-gray-700" draggable="true" @dragstart="(ev) => canvasStore.handleDragStart(ev, component.name)" @dragend="(_ev) => canvasStore.handleDragEnd()">
					<div class="w-full flex flex-col items-center justify-center gap-2 truncate rounded border-[1px] border-gray-300 bg-gray-50 p-4 transition duration-300 ease-in-out">
						<LucideIcon :name="component.icon" class="h-6 w-6" />
					</div>
					<span class="truncate text-xs">{{ component.title }}</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { computed, ref } from "vue"
import { TextInput } from "frappe-ui"

import components from "@/data/components"


import LucideIcon from "@/components/LucideIcon.vue"
import useCanvasStore from "@/stores/canvasStore"
import useStudioStore from "@/stores/studioStore"
import { isObjectEmpty } from "@/utils/helpers"
import { StudioPage } from "@/types/Studio/StudioPage"

const canvasStore = useCanvasStore()
const store = useStudioStore()

const isAppHome = (page: StudioPage) => store.activeApp?.app_home === page.name

const componentFilter = ref("")
const componentList = computed(() => {
	if (componentFilter.value) {
		return components.list.filter((component) =>
			component.name?.toLowerCase().includes(componentFilter.value.toLowerCase()),
		)
	} else {
		return components.list
	}
})

const getComponentMenu = (component?: string) => {
	if (isObjectEmpty(store.activeApp)) return []

	const app = store.activeApp!

	return [
		{
			label: "Rename",
			icon: "type",
			// condition: () => !isAppHome(page),
			onClick: () => {
				// store.setAppHome(app.name, page.name)
			},
		},
		{
			label: "Modify",
			icon: "edit",
			onClick: () => {
				// store.duplicateAppPage(app.name, page),
			},
		},
		{
			label: "Delete",
			icon: "trash",
			onClick: async () => {
				// await store.deleteAppPage(app.name, page)
				// if (isPageActive(page)) {
				// 	router.push({
				// 		name: "StudioPage",
				// 		params: { appID: app.name, pageID: app.app_home },
				// 		replace: true,
				// 	})
				// }
			},
		},
	]
}


</script>
