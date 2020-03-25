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
// BtpArgumentDeclaration232AllOf struct for BtpArgumentDeclaration232AllOf
type BtpArgumentDeclaration232AllOf struct {
	StandardType string `json:"standardType,omitempty"`
	TypeName string `json:"typeName,omitempty"`
	Name BtpIdentifier8 `json:"name,omitempty"`
	Type BtpTypeName290 `json:"type,omitempty"`
	BtType string `json:"btType,omitempty"`
}
