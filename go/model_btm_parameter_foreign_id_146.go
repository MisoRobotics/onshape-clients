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
// BtmParameterForeignId146 struct for BtmParameterForeignId146
type BtmParameterForeignId146 struct {
	BtType string `json:"btType,omitempty"`
	ImportMicroversion string `json:"importMicroversion,omitempty"`
	NodeId string `json:"nodeId,omitempty"`
	ParameterId string `json:"parameterId,omitempty"`
	ForeignId string `json:"foreignId,omitempty"`
	LocationInfo BtForeignDataResponse1070 `json:"locationInfo,omitempty"`
	ForeignName string `json:"foreignName,omitempty"`
}
