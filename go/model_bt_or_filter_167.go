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
// BtOrFilter167 struct for BtOrFilter167
type BtOrFilter167 struct {
	BtType string `json:"btType,omitempty"`
	Operand1 BtQueryFilter183 `json:"operand1,omitempty"`
	Operand2 BtQueryFilter183 `json:"operand2,omitempty"`
}
