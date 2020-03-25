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
// BtpTopLevelNode286AllOf struct for BtpTopLevelNode286AllOf
type BtpTopLevelNode286AllOf struct {
	Deprecated bool `json:"deprecated,omitempty"`
	SymbolName BtpIdentifier8 `json:"symbolName,omitempty"`
	ArgumentsToDocument []BtpArgumentDeclaration232 `json:"argumentsToDocument,omitempty"`
	DeprecatedExplanation string `json:"deprecatedExplanation,omitempty"`
	ForExport bool `json:"forExport,omitempty"`
	SpaceAfterExport BtpSpace10 `json:"spaceAfterExport,omitempty"`
	Annotation BtpAnnotation231 `json:"annotation,omitempty"`
	BtType string `json:"btType,omitempty"`
}
