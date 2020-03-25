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
// BtmSketchTextEntity1761 struct for BtmSketchTextEntity1761
type BtmSketchTextEntity1761 struct {
	BtType string `json:"btType,omitempty"`
	ControlBoxIds []string `json:"controlBoxIds,omitempty"`
	EntityId string `json:"entityId,omitempty"`
	EntityIdAndReplaceInDependentFields string `json:"entityIdAndReplaceInDependentFields,omitempty"`
	ImportMicroversion string `json:"importMicroversion,omitempty"`
	IsConstruction bool `json:"isConstruction,omitempty"`
	Namespace string `json:"namespace,omitempty"`
	NodeId string `json:"nodeId,omitempty"`
	Parameters []BtmParameter1 `json:"parameters,omitempty"`
	FontName string `json:"fontName,omitempty"`
	Text string `json:"text,omitempty"`
	Ascent float64 `json:"ascent,omitempty"`
	BaselineStartX float64 `json:"baselineStartX,omitempty"`
	BaselineStartY float64 `json:"baselineStartY,omitempty"`
	BaselineDirectionX float64 `json:"baselineDirectionX,omitempty"`
	BaselineDirectionY float64 `json:"baselineDirectionY,omitempty"`
}
