/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// BtBillOfMaterialsUniqueItemId2029 struct for BtBillOfMaterialsUniqueItemId2029
type BtBillOfMaterialsUniqueItemId2029 struct {
	AmbiguousUniqueId BtBillOfMaterialsUniqueItemId2029 `json:"ambiguousUniqueId,omitempty"`
	ApiConfiguration string `json:"apiConfiguration,omitempty"`
	BtType string `json:"btType,omitempty"`
	DocumentVersionElementId BtDocumentVersionElementIds1897 `json:"documentVersionElementId,omitempty"`
	ElementId string `json:"elementId,omitempty"`
	FullElementId BtFullElementId756 `json:"fullElementId,omitempty"`
	IsStandardContent bool `json:"isStandardContent,omitempty"`
	ItemDefinitionId string `json:"itemDefinitionId,omitempty"`
	NonGeometric bool `json:"nonGeometric,omitempty"`
	PartId string `json:"partId,omitempty"`
	SourceElement BtElementReference725 `json:"sourceElement,omitempty"`
	StandardContentOwner BtOwner3114 `json:"standardContentOwner,omitempty"`
	UniqueElementId BtBillOfMaterialsUniqueItemId2029 `json:"uniqueElementId,omitempty"`
	VersionId string `json:"versionId,omitempty"`
	WorkspacePartItem bool `json:"workspacePartItem,omitempty"`
	WorkspaceReference bool `json:"workspaceReference,omitempty"`
}
